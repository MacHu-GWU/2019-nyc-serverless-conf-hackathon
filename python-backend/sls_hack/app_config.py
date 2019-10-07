# -*- coding: utf-8 -*-

from lbdrabbit import AppConfig, Constant, Derivable


class SlsHackAppConfig(AppConfig):
    DYNAMODB_TABLE_NAME_GPS_TRACKER = Derivable()

    @DYNAMODB_TABLE_NAME_GPS_TRACKER.getter
    def get_DYNAMODB_TABLE_NAME_GPS_TRACKER(self):
        return "{}-gps-tracker".format(self.ENVIRONMENT_NAME.get_value())

    DYNAMODB_TABLE_NAME_DEVICE_STATUS= Derivable()

    @DYNAMODB_TABLE_NAME_DEVICE_STATUS.getter
    def get_DYNAMODB_TABLE_NAME_DEVICE_STATUS(self):
        return "{}-device-status".format(self.ENVIRONMENT_NAME.get_value())

