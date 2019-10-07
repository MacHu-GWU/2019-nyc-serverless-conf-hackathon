Crime Alert For Parent to protect Kids from Dangerous Zipcode
==============================================================================

.. contents::
    :local:


What Problem Does this App Solve
------------------------------------------------------------------------------

**Send Notification to Parent when Kids going to a Dangerous Zipcode, High Rate on Crime Report**.

Dataset: Jan to June, 223,000 crime report data

- https://www1.nyc.gov/site/nypd/stats/crime-statistics/citywide-crime-stats.page

Demo App:

- App Endpoint: http://ui-nyc-serverless-conf-hackathon.s3-website-us-east-1.amazonaws.com/#/login
- Login: both ``dd@dd.com``

Test Case:

- device_id = "de042ca7-3bd0-4d66-8690-d88312d18cef"
- lat, lng = 40.698773, -73.833735  # 11418 Safe
- lat, lng = 40.672593, -73.874493  # 11208 VERY DANGEROUS

Cross Validation:

- NYC Crime Map: https://maps.nyc.gov/crime/
- Google Map: https://www.google.com/maps/place/40%C2%B041'55.6%22N+73%C2%B050'01.5%22W/@40.698773,-73.8359237,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d40.698773!4d-73.833735


It is a General Used Architect for Geo location Based Notificagtion App
------------------------------------------------------------------------------

More Notification could be implemented with this Architect. we can use for traffic accident, tourism industry (interesting place near by), etc ...

- Api Gateway for IOT Devices: https://console.aws.amazon.com/apigateway/home?region=us-east-1#/apis/69kusj68ik/resources/ffx67ddjki
- Lambda Function for Notification Event and ETL: https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/sls-hack-dev-rpc-gps-tracker-handler?tab=configuration
- DynamoDB for App Data: https://console.aws.amazon.com/dynamodb/home?region=us-east-1#tables:selected=sls-hack-dev-gps-tracker;tab=items
- Kinesis Stream ETL: https://console.aws.amazon.com/kinesis/home?region=us-east-1#/dashboard
- Athena Table for ETL work, Data Lake to Data warehouse: https://console.aws.amazon.com/athena/home?force&region=us-east-1#query
- S3 Bucket for Raw Data: https://s3.console.aws.amazon.com/s3/buckets/eq-hackathon-sls-hack-dev-raw-data/data/crime/?region=us-east-1&tab=overview
- CloudFormation: https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/events?filteringText=sls-hack&filteringStatus=active&viewNested=false&hideStacks=false&stackId=arn%3Aaws%3Acloudformation%3Aus-east-1%3A700621413265%3Astack%2Fsls-hack-dev%2Fbe7dd260-e916-11e9-9b1b-0ea1c9c8db82
- SNS for Mobile Notification.


Tech Innovation 1. Infrastructure as Code for Real
------------------------------------------------------------------------------

- troposphere_mate, real IAC, cloudformation orchestration: https://github.com/MacHu-GWU/troposphere_mate-project
- lbdrabbit, no handy Cloudformation, No serverless.yml, No sam.yml.: https://github.com/MacHu-GWU/lbdrabbit-project
- configirl: https://github.com/MacHu-GWU/configirl-project

- Auto Api Gateway Integration Example: https://github.com/MacHu-GWU/lbdrabbit-project/tree/master/lbdrabbit/example/handlers


Tech Innovation 2. Open Source US zipcode Geograph, Demographics, Economic, Eduation Statistics Database
------------------------------------------------------------------------------

- uszipcode: https://github.com/MacHu-GWU/uszipcode-project
