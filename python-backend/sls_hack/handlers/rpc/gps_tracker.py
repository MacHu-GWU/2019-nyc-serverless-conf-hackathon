# -*- coding: utf-8 -*-

import json
from sls_hack.model.gps_tracker import GpsTracker


def handler(event, context):
    item = GpsTracker(**event)
    dynamodb_save_response = item.save()
    return {
        "status_code": "200",
        "body": json.dumps({
            "event": event,
            "dynamodb_save_response": dynamodb_save_response,
        })
    }
