# -*- coding: utf-8 -*-

import json
import boto3
from sls_hack.app_config_init import app_config
from sls_hack.model.gps_tracker import GpsTracker, DeviceStatus, ZipcodeCrimeIndex
from sls_hack.helpers import find_zipcode_by_lat_lng
from sls_hack.logger import stream_logger as logger

boto_ses = boto3.session.Session(profile_name=app_config.AWS_PROFILE_FOR_BOTO3.get_value())


def handler(event, context):
    item = GpsTracker(**event)
    logger.info("received {}".format(event))
    item.save()

    current_zipcode = find_zipcode_by_lat_lng(event["lat"], event["lng"])
    logger.info("current zipcode is {}".format(current_zipcode))

    send_notification_flag = False
    device_status = DeviceStatus.get(hash_key=event["device_id"])
    previous_zipcode = device_status.current_zipcode
    if device_status.current_zipcode != current_zipcode:
        logger.info("current zipcode changed from {} to {}".format(
            device_status.current_zipcode,
            current_zipcode,
        ))
        device_status.current_zipcode = current_zipcode
        device_status.save()

        # TODO: detect if it is a dangerous zipcode
        zipcode_crime_index = ZipcodeCrimeIndex.get(hash_key=current_zipcode)
        if zipcode_crime_index.crime_index in ["DANGEROUS", "VERY DANGEROUS"]:
            send_notification_flag = True

        logger.info("current zipcode crime level is {}".format(zipcode_crime_index.crime_index))
    else:
        logger.info("zipcode not changed")

    if send_notification_flag is True:
        sns_client = boto_ses.client("sns")
        res = sns_client.publish(
            Message="Warning {username}, you are entering zipcode {zipcode}, which is highly dangerous!".format(
                username=device_status.username,
                zipcode=current_zipcode,
            ),
            PhoneNumber=device_status.phone_number,
        )
        logger.info("sns publish response {}".format(res))

    body_data = {
        "event": event,
        "previous_zipcode": previous_zipcode,
        "current_zipcode": current_zipcode,
        "is_alert_sent": send_notification_flag,
    }

    body = json.dumps(body_data, indent=4)

    logger.info("response {}".format(body))

    return {
        "status_code": "200",
        "body": body
    }


if __name__ == "__main__":
    from datetime import datetime

    # print(uuid.uuid4())
    device_id = "de042ca7-3bd0-4d66-8690-d88312d18cef"
    create_at = str(datetime.utcnow())
    # lat, lng = 40.698773, -73.833735  # 11418 Safe
    lat, lng = 40.672593, -73.874493  # 11208 VERY DANGEROUS

    event = dict(
        device_id=device_id,
        create_at=create_at,
        lat=lat, lng=lng,
    )
    handler(event, {})
