# -*- coding: utf-8 -*-

import boto3
from .app_config_init import app_config

boto_ses = boto3.session.Session(profile_name=app_config.AWS_PROFILE_FOR_BOTO3.get_value())
