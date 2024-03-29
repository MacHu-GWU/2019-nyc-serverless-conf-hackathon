# -*- coding: utf-8 -*-

from sls_hack import __version__
from .app_config import SlsHackAppConfig

app_config = SlsHackAppConfig()
app_config.PROJECT_NAME.set_value("sls_hack")
app_config.STAGE.set_value("dev")
app_config.HANDLER_MODULE_NAME.set_value("lbdrabbit.example.handlers")
app_config.S3_BUCKET_FOR_DEPLOY.set_value("eq-hackathon-for-everything")
app_config.LAMBDA_CODE_S3_BUCKET.set_value(app_config.S3_BUCKET_FOR_DEPLOY.get_value())
app_config.LAMBDA_CODE_S3_KEY.set_value("lambda/MacHu-GWU/sls_hack-project/{}/source.zip".format(__version__))
app_config.LAMBDA_LAYER_ARN.set_value([
    "arn:aws:lambda:us-east-1:700621413265:layer:sls_hack:6"
])
app_config.AWS_PROFILE_FOR_DEPLOY.set_value("eq_hack")
