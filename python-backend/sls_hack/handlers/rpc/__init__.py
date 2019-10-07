# -*- coding: utf-8 -*-

from lbdrabbit import LbdFuncConfig

__lbd_func_config__ = LbdFuncConfig()
__lbd_func_config__.apigw_resource_yes = True
__lbd_func_config__.apigw_method_yes = True
__lbd_func_config__.apigw_method_int_type = LbdFuncConfig.ApiMethodIntType.rpc
__lbd_func_config__.apigw_method_enable_cors_yes = True
