#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/8/25 16:51
# @Author : Greey
# @FileName: Test_Unbind_Device.py


'''
测试步骤：
1：登录App（获取平台token）
2：解除绑定手环

预期结果：
1：成功登录App，并返回token值
2：成功解除绑定手环，响应信息返回"message : OK"

'''


import pytest
import os
import sys
import allure
from ApiTest.Common.Config import ReadConfig
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Request import Request
from ApiTest.Common.Log import MyLog
from ApiTest.Common.Assert import Assertions
from ApiTest.Common.Session import Session
from ApiTest.Common.Module import Moudle

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "..")
config_path = father_path + "\\" + "Config\\Config.ini"
yaml_path = father_path + "\\" + "Testdata\\unbind_device.yaml"



@allure.feature('解除绑定手环')
@allure.description('验证不同场景解除绑定手环')
class TestClass:
    def setup(self):
        print("Test Start")
        self.config = ReadConfig(config_path)
        self.login_host = self.config.get_value("Wristband_Alpha", "host")
        self.login_host = self.login_host.encode('utf-8')                                                             #config文件获取host

        self.yaml = Yamlc(yaml_path).get_yaml_data(1, "unbind_device")
        self.method = Yamlc(yaml_path).get_yaml_data(1, "unbind_device", "method")
        self.url = Yamlc(yaml_path).get_yaml_data(1, "unbind_device", "url")
        self.parm = Yamlc(yaml_path).get_yaml_data(1, "unbind_device", "parm")
        self.expect = Yamlc(yaml_path).get_yaml_data(1, "unbind_device", "expect")                                  #yaml文件获取传入参数

        self.url = self.login_host + self.url
        self.log = MyLog()
        self.log.debug(u'初始化测试数据')

    def teardown(self):
        print("Test End")

    case_name = Yamlc(yaml_path).get_yaml_data(1, "unbind_device", "case_name")
    @allure.story(case_name)
    @allure.severity('blocker')
    def test_unbind_device001(self):
        Returndata = Moudle().bind_device()
        self.parm['device_token'] = Returndata[0]
        self.headers = Returndata[1]
        r = Request().post_wirst_request(method=self.method, url=self.url, data=self.parm, header=self.headers)
        print(r)
        Assertions().assert_code(r['code'], self.expect['code'])
        Assertions().assert_code(r['status_code'], self.expect['status_code'])
        Assertions().assert_time(r['time_total'], self.expect['respones_time'])
        Assertions().assert_code(r['message'], self.expect['message'])
        Assertions().assert_code(r['data'], self.expect['data'])

if __name__ == '__main__':
     pytest.main()
