# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from sls_hack.app_config import AppConfig

class TestAppConfig(object):
    pass


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
