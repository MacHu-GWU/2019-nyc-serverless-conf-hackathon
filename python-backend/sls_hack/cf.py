# -*- coding: utf-8 -*-

import troposphere_mate as tm
from troposphere_mate import apigateway, awslambda, iam, dynamodb, kinesis, s3, glue, firehose
from troposphere_mate import Ref, GetAtt, Sub, AWS_ACCOUNT_ID
from troposphere_mate.canned.iam import AWSManagedPolicyArn, AWSServiceName, create_assume_role_policy_document
from .app_config_init import app_config

template = tm.Template()

param_env_name = tm.Parameter(
    "EnvironmentName",
    Type="String",
)
template.add_parameter(param_env_name)

rest_api = apigateway.RestApi(
    "RestApi",
    template=template,
    Name=tm.helper_fn_sub("{}", param_env_name),
    EndpointConfiguration=apigateway.EndpointConfiguration(
        Types=["REGIONAL", ]
    )
)

lambda_code = awslambda.Code(
    S3Bucket=app_config.LAMBDA_CODE_S3_BUCKET.get_value(),
    S3Key=app_config.LAMBDA_CODE_S3_KEY.get_value(),
)

iam_role = iam.Role(
    "IamRoleForLbdFunc",
    template=template,
    RoleName=tm.helper_fn_sub("{}-lbd-func", param_env_name),
    AssumeRolePolicyDocument=create_assume_role_policy_document([
        AWSServiceName.aws_Lambda
    ]),
    ManagedPolicyArns=[
        AWSManagedPolicyArn.administratorAccess,
    ]
)

dynamodb_table_gps_tracker = dynamodb.Table(
    "DynamodbTableGpsTracker",
    template=template,
    TableName=app_config.DYNAMODB_TABLE_NAME_GPS_TRACKER.get_value(),
    KeySchema=[
        dynamodb.KeySchema(
            AttributeName="device_id",
            KeyType="HASH",
        ),
        dynamodb.KeySchema(
            AttributeName="create_at",
            KeyType="RANGE",
        ),
    ],
    AttributeDefinitions=[
        dynamodb.AttributeDefinition(
            AttributeName="device_id",
            AttributeType="S",
        ),
        dynamodb.AttributeDefinition(
            AttributeName="create_at",
            AttributeType="S",
        ),
    ],
    BillingMode="PAY_PER_REQUEST",
)
"""
Device location history.
"""

dynamodb_table_device_status = dynamodb.Table(
    "DynamodbTableDeviceStatus",
    template=template,
    TableName=app_config.DYNAMODB_TABLE_NAME_DEVICE_STATUS.get_value(),
    KeySchema=[
        dynamodb.KeySchema(
            AttributeName="device_id",
            KeyType="HASH",
        ),
    ],
    AttributeDefinitions=[
        dynamodb.AttributeDefinition(
            AttributeName="device_id",
            AttributeType="S",
        ),
    ],
    BillingMode="PAY_PER_REQUEST",
)
"""
Provide lastest status information about a device.
"""

dynamodb_table_zipcode_crime_index = dynamodb.Table(
    "DynamodbTableZipcodeCrimeIndex",
    template=template,
    TableName=app_config.DYNAMODB_TABLE_NAME_ZIPCODE_CRIME_INDEX.get_value(),
    KeySchema=[
        dynamodb.KeySchema(
            AttributeName="zipcode",
            KeyType="HASH",
        ),
    ],
    AttributeDefinitions=[
        dynamodb.AttributeDefinition(
            AttributeName="zipcode",
            AttributeType="S",
        ),
    ],
    BillingMode="PAY_PER_REQUEST",
)
"""
Provide zipcode crime index information for alerting.
Update regularly from raw dataset.
"""

s3_bucket_for_raw_data = s3.Bucket(
    "S3BucketForEventRawData",
    template=template,
    BucketName=tm.helper_fn_sub("eq-hackathon-{}-raw-data", param_env_name),
)

kinesis_stream_raw_data_in = kinesis.Stream(
    "KinesisStreamRawDataIn",
    template=template,
    Name=tm.helper_fn_sub("{}-raw-data-in", param_env_name),
    ShardCount=2,
)

kinesis_firehose_delivery_stream_etl = firehose.DeliveryStream(
    "KinesisFirehoseDeliveryStreamEtl",
    template=template,
    DeliveryStreamName=tm.helper_fn_sub("{}-etl", param_env_name),
    DeliveryStreamType="KinesisStreamAsSource",
    KinesisStreamSourceConfiguration=firehose.KinesisStreamSourceConfiguration(
        KinesisStreamARN=GetAtt(kinesis_stream_raw_data_in, "Arn"),
        RoleARN="arn:aws:iam::700621413265:role/firehose-admin-role",
    ),
    ExtendedS3DestinationConfiguration=firehose.ExtendedS3DestinationConfiguration(
        BucketARN=GetAtt(s3_bucket_for_raw_data, "Arn"),
        BufferingHints=firehose.BufferingHints(
            IntervalInSeconds=60,
            SizeInMBs=6,
        ),
        CompressionFormat="UNCOMPRESSED",
        RoleARN="arn:aws:iam::700621413265:role/firehose-admin-role",
    ),
)

athena_database = glue.Database(
    "AthenaDatabase",
    template=template,
    CatalogId=Ref(AWS_ACCOUNT_ID),
    DatabaseInput=glue.DatabaseInput(
        Name=app_config.ENVIRONMENT_NAME.get_value().replace("-", "_")
    ),
)
