# -*- coding: utf-8 -*-

import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from sls_hack.app_config_init import app_config

if not app_config.is_aws_lambda_runtime():
    os.environ["AWS_DEFAULT_PROFILE"] = app_config.AWS_PROFILE_FOR_DEPLOY.get_value()


class GpsTracker(Model):
    class Meta:
        table_name = app_config.DYNAMODB_TABLE_NAME_GPS_TRACKER.get_value()

    device_id = UnicodeAttribute(range_key=True)
    create_at = UnicodeAttribute(hash_key=True)
    lat = NumberAttribute(null=False)
    lng = NumberAttribute(null=False)


if __name__ == "__main__":
    import uuid
    from datetime import datetime

    print(uuid.uuid4())
    device_id = "de042ca7-3bd0-4d66-8690-d88312d18cef"
    create_at = str(datetime.utcnow())
    print(create_at)
    lat, lng = 40.702962, -74.011626
    item = GpsTracker(
        device_id=device_id,
        create_at=create_at,
        lat=lat, lng=lng,
    )
    # response = item.save()
    # print(response)
