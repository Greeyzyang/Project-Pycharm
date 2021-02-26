#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/11/7 22:00
# @Author : Greey
# @FileName: Concurrent_Test.py

import pytest
import os
import time
import allure
from ApiTest.Common.appcommon import App
from ApiTest.Common.Readyaml import Yamlc
from ApiTest.Common.Log import MyLog
from selenium.webdriver.common.by import By
import multiprocessing


current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "../..")                                  #获取上上级目录
yaml_path = father_path + "\\" + "Testdata\\app.yaml"

class Testsmoke:

    def __init__(self):
        self.log = MyLog()
        self.log.info('初始化测试数据')
        self.dictdatas = Yamlc(yaml_path).get_allyaml_data("Model")
        self.init_port = 4723
        self.init_systemPort = 8200
        self.section = 'SATURN_设备'
        self.mac1 = '2C:AA:8E:8F:71:30'
        self.mac2 = '2C:AA:8E:8F:71:30'
        self.mac3 = '2C:AA:8E:8F:72:04'
        self.mac4 = '2C:AA:8E:8F:0F:A2'
        self.mac5 = '2C:AA:8E:8F:71:30'
        self.mac6 = '2C:AA:8E:8F:71:30'
        self.mac7 = '2C:AA:8E:8F:0F:A2'
    def smoke1(self):
        info = "Process-1"
        self.port = self.init_port
        self.systemPort = self.init_systemPort
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[0]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(2)
        app.open_application(self.port)
        app.devices_bind_ota(self.mac1, self.section, info)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '心率运行次数：' + str(i))
                # app.device_leftslide()
                # self.log.debug(info + "向左滑动成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.saturn_inputclick("80", "240", "80", "240")
                self.log.debug(info + "点击心率icon成功")
                app.assert_getdevicepagename("hrm")
                self.log.debug(info + "进入心率功能成功")
                time.sleep(5)
                app.device_home()
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回表盘页面成功")
                # app.device_home()
                # self.log.debug(info + "home键进入菜单页面")
                # app.saturn_inputclick("240", "240", "240", "240")
                # self.log.debug(info + "点击血氧icon成功")
                # app.assert_getdevicepagename("spo2")
                # self.log.debug(info + "进入血氧功能成功")
                # time.sleep(5)
                # app.device_home()
                # app.assert_getdevicepagename("home_page")
                # self.log.debug(info + "返回表盘页面成功")
            except:
                self.log.error(info + '心率在第N次运行失败：' + str(i))
                app.call_back_brandy(self.mac1, self.section, self.port, self.uuid)
    def smoke2(self):
        info = "Process-2"
        print(info)
        self.port = int(self.init_port) + 2
        self.systemPort = int(self.init_systemPort) + 2
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[1]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(2)
        app.open_application(self.port)
        # size = driver1.get_window_size()
        app.devices_bind_ota(self.mac2, self.section, info)
        # app1.swpe(size['width']*0.25, size['height']*0.95, size['width']*0.25, size['height']*0.25)
        # for i in range(1, 1000):
        #     try:
        #         self.log.debug(info + '切换表盘运行次数：' + str(i))
        #         for m in range(1, 6):
        #             app.device_longpress()
        #             self.log.debug(info + "长按进入切换表盘页面成功")
        #             app.device_leftslide()
        #             self.log.debug(info + "向左滑动成功")
        #             app.saturn_inputclick("160", "160", "160", "160")
        #             self.log.debug(info + "点击表盘成功")
        #             app.assert_getdevicepagename("home_page")
        #             self.log.debug(info + "退出切换表盘页面成功")
        #         for n in range(1, 6):
        #             app.device_longpress()
        #             self.log.debug(info + "长按进入切换表盘页面成功")
        #             app.device_rightslide()
        #             self.log.debug(info + "向右滑动成功")
        #             app.saturn_inputclick("160", "160", "160", "160")
        #             self.log.debug(info + "点击表盘成功")
        #             app.assert_getdevicepagename("home_page")
        #             self.log.debug(info + "退出切换表盘页面成功")
        #     except:
        #         self.log.error(info + '切换表盘在第N次运行失败：' + str(i))
        #         app.call_back_brandy(self.mac2, self.section, self.port, self.uuid)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '心率运行次数：' + str(i))
                # app.device_leftslide()
                # self.log.debug(info + "向左滑动成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.saturn_inputclick("80", "240", "80", "240")
                self.log.debug(info + "点击心率icon成功")
                app.assert_getdevicepagename("hrm")
                self.log.debug(info + "进入心率功能成功")
                time.sleep(5)
                app.device_home()
                app.assert_getdevicepagename("home_page")
                self.log.debug(info + "返回表盘页面成功")
                # app.device_home()
                # self.log.debug(info + "home键进入菜单页面")
                # app.saturn_inputclick("240", "240", "240", "240")
                # self.log.debug(info + "点击血氧icon成功")
                # app.assert_getdevicepagename("spo2")
                # self.log.debug(info + "进入血氧功能成功")
                # time.sleep(5)
                # app.device_home()
                # app.assert_getdevicepagename("home_page")
                # self.log.debug(info + "返回表盘页面成功")
            except:
                self.log.error(info + '心率在第N次运行失败：' + str(i))
                app.call_back_brandy(self.mac2, self.section, self.port, self.uuid)

    def smoke3(self):
        info = "Process-3"
        print(info)
        self.port = int(self.init_port) + 4
        self.systemPort = int(self.init_systemPort) + 4
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[0]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(2)
        app.open_application(self.port)
        app.devices_bind_ota(self.mac3, self.section)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '进出各个应用运行次数：' + str(i))
                app.device_home()
                self.log.debug(info + "HOME键进入菜单")
                app.saturn_inputclick("80", "80", "80", "80")
                self.log.debug(info + "点击数据icon成功")
                app.assert_getdevicepagename("data_page")
                self.log.debug(info + "进入数据功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
                app.device_home()
                self.log.debug(info + "HOME键进入菜单")
                app.saturn_inputclick("240", "80", "240", "80")
                self.log.debug(info + "点击运动icon成功")
                app.assert_getdevicepagename("sports")
                self.log.debug(info + "进入运动功能成功")
                time.sleep(3)
                app.device_home()
                self.log.debug(info + "退出运动功能")
                app.saturn_inputclick("80", "160", "80", "160")
                self.log.debug(info + "点击Finish")
                app.saturn_inputclick("280", "280", "280", "280")
                self.log.debug(info + "点击Confirm")
                app.saturn_inputclick("80", "240", "80", "240")
                self.log.debug(info + "点击心率icon成功")
                app.assert_getdevicepagename("hrm")
                self.log.debug(info + "进入心率功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.saturn_inputclick("240", "240", "240", "240")
                self.log.debug(info + "点击血氧icon成功")
                app.assert_getdevicepagename("spo2")
                self.log.debug(info + "进入血氧功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("80", "80", "80", "80")
                self.log.debug(info + "点击闹钟icon成功")
                app.assert_getdevicepagename("alarm")
                self.log.debug(info + "进入闹钟功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("240", "80", "240", "80")
                self.log.debug(info + "点击倒计时icon成功")
                app.assert_getdevicepagename("timer")
                self.log.debug(info + "进入倒计时功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("80", "240", "80", "240")
                self.log.debug(info + "点击天气icon成功")
                app.assert_getdevicepagename("weather")
                self.log.debug(info + "进入天气功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("240", "240", "240", "240")
                self.log.debug(info + "点击Shortcut icon成功")
                app.assert_getdevicepagename("shortcut_page")
                self.log.debug(info + "进入Shortcut功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("80", "240", "80", "240")
                self.log.debug(info + "点击女性健康icon成功")
                app.assert_getdevicepagename("period")
                self.log.debug(info + "进入女性健康功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
                app.device_home()
                self.log.debug(info + "home键进入菜单页面")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("240", "240", "240", "240")
                self.log.debug(info + "点击设置icon成功")
                app.assert_getdevicepagename("setting_page")
                self.log.debug(info + "进入设置功能成功")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
            except:
                self.log.error(info + '进出各个应用在第N次运行失败：' + str(i))
                app.call_back_brandy(self.mac3, self.section, self.port, self.uuid)


    def smoke4(self):
        info = "Process-4"
        self.port = int(self.init_port) + 6
        self.systemPort = int(self.init_systemPort) + 6
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[2]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(2)
        driver = app.open_application(self.port)
        app.devices_bind_ota(self.mac4, self.section)
        i = 0
        for i in range(1, 1000):
            try:
                self.log.debug(info + '运动中发送短信/消息/电话运行次数：' + str(i))
                app.device_home()
                self.log.debug(info + "HOME键进入菜单")
                app.saturn_inputclick("240", "80", "240", "80")
                self.log.debug(info + "点击运动icon成功")
                app.assert_getdevicepagename("sports")
                self.log.debug(info + "进入运动功能成功")
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_send_notification('{"appMessage": {"appId": "app.wx", "text": "ryeex' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                self.log.debug(info + '发送消息次数' + str(i))
                time.sleep(3)
                app.tv_send_notification('{"sms": {"contact": "ryeex' + str(i) + '", "content": "ryeex' + str(i) + '", "sender": ' + str(i) + '}, "type": "SMS"}')
                self.log.debug(info + '发短信次数' + str(i))
                time.sleep(3)
                app.tv_send_notification('{"telephony": {"contact": "ryeex' + str(i) + '", "number": ' + str(i) + ', "status": "RINGING_UNANSWERABLE"}, "type": "TELEPHONY"}')
                self.log.debug(info + '打电话次数' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.assert_getdevicepagename("remind")
                self.log.debug(info + '进入提醒页面成功')
                app.device_home()
                app.assert_getdevicepagename("sports")
                self.log.debug(info + '退出提醒页面成功')
                app.device_home()
                self.log.debug(info + "退出运动功能")
                app.saturn_inputclick("80", "160", "80", "160")
                self.log.debug(info + "点击Finish")
                app.saturn_inputclick("280", "280", "280", "280")
                self.log.debug(info + "点击Confirm")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
            except:
                self.log.error(info + '运动中发送消息在第N次运行失败：' + str(i))
                app.call_back_brandy(self.mac4, self.section, self.port, self.uuid)

    def smoke5(self):
        info = "Process-5"
        self.port = int(self.init_port) + 8
        self.systemPort = int(self.init_systemPort) + 8
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[0]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(2)
        driver = app.open_application(self.port)
        app.devices_bind_ota(self.mac5, self.section)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '查看消息运行次数：' + str(i))
                driver.keyevent(4)
                app.devices_click('SATURN_APP')
                app.click_prompt_box()
                app.click_prompt_box()
                app.click_prompt_box()
                app.tv_send_notification('{"appMessage": {"appId": "app.facebook", "text": "reeyx' + str(i) + '", "title": ' + str(i) + '}, "type": "APP_MESSAGE"}')
                self.log.debug(info + '发送通知成功')
                driver.keyevent(4)
                app.devices_click('SATURN_设备')
                app.assert_getdevicepagename('remind')
                self.log.debug(info + '进入消息详情页面成功')
                app.device_home()
                self.log.debug(info + '返回主页面成功')
                app.assert_getdevicepagename("home_page")
                app.device_downslide()
                self.log.debug(info + '向下滑动成功')
                self.log.debug(info + "返回到消息页面")
                app.saturn_inputslide("160", "20", "160", "160")
                self.log.debug(info + '向下滑动一段距离')
                app.saturn_inputslide("160", "160", "160", "20")
                self.log.debug(info + '向上滑动一段距离')
                app.saturn_inputclick("160", "160", "160", "160")
                self.log.debug(info + '查看消息')
                app.assert_getdevicepagename('notification_box_detail')
                self.log.debug(info + '进入消息详情页面成功')
                app.device_home()
                self.log.debug(info + "返回")
                app.assert_getdevicepagename('home_page')
                self.log.debug(info + '退出消息页面成功')
            except:
                self.log.error(info + '查看消息在第N次运行失败：' + str(i))
                app.call_back_brandy(self.mac5, self.section, self.port, self.uuid)


    def smoke6(self):
        info = "Process-6"
        print(info)
        self.port = int(self.init_port) + 10
        self.systemPort = int(self.init_systemPort) + 10
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[1]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(2)
        driver = app.open_application(self.port)
        app.devices_bind_ota(self.mac6, self.section)
        for i in range(1, 1000):
            try:
                self.log.debug(info + '进入各个倒计时次数：' + str(i))
                app.device_home()
                self.log.debug(info + "HOME键进入菜单")
                app.device_upslide()
                self.log.debug(info + "向上滑动成功")
                app.saturn_inputclick("240", "80", "240", "80")
                self.log.debug(info + "点击倒计时icon成功")
                app.assert_getdevicepagename("timer")
                self.log.debug(info + "进入倒计时功能成功")
                app.saturn_inputclick("80", "80", "80", "80")
                self.log.debug(info + "选择1分钟")
                app.saturn_inputclick("80", "300", "80", "300")
                self.log.debug(info + "点击stop")
                app.saturn_inputclick("240", "80", "240", "80")
                self.log.debug(info + "选择3分钟")
                app.saturn_inputclick("80", "300", "80", "300")
                self.log.debug(info + "点击stop")
                app.saturn_inputclick("80", "240", "80", "240")
                self.log.debug(info + "选择5分钟")
                app.saturn_inputclick("80", "300", "80", "300")
                self.log.debug(info + "点击stop")
                app.saturn_inputclick("240", "240", "240", "240")
                self.log.debug(info + "选择10分钟")
                app.saturn_inputclick("80", "300", "80", "300")
                self.log.debug(info + "点击stop")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
            except:
                self.log.error(info + '进入各个倒计时在第N次运行失败：' + str(i))
                app.call_back_brandy(self.mac6, self.section, self.port, self.uuid)


    def smoke7(self):
        info = "Process-7"
        self.port = int(self.init_port) + 12
        self.systemPort = int(self.init_systemPort) + 12
        desired_cap = self.dictdatas[0]['desired_caps']
        uuid = App(desired_cap).getdevices_uuid()[2]
        self.uuid = uuid
        andriod_version = App(desired_cap).getdevice_version(uuid)
        print(info + "设备ID:" + uuid)
        print(info + "安卓版本:" + andriod_version)
        desired_cap['deviceName'] = uuid
        desired_cap['platformVersion'] = andriod_version
        desired_cap['systemPort'] = self.systemPort
        App(desired_cap).start_appium(self.port, int(self.port) + 1, uuid)
        app = App(desired_cap)
        time.sleep(2)
        driver = app.open_application(self.port)
        app.devices_bind_ota(self.mac7, self.section)
        for i in range(1, 2):
            try:
                app.device_home()
                self.log.debug(info + "HOME键进入菜单")
                app.saturn_inputclick("240", "80", "240", "80")
                self.log.debug(info + "点击运动icon成功")
                app.assert_getdevicepagename("sports")
                self.log.debug(info + "进入运动功能成功")
                # time.sleep(300)
                for j in range(1, 5000):
                    self.log.debug(info + '：暂定运动次数' + str(j))
                    app.device_home()
                    self.log.debug(info + "退出运动功能")
                    app.device_home()
                    app.saturn_inputclick("240", "160", "240", "160")
                    self.log.debug(info + "点击Continue")
                    app.device_home()
                    self.log.debug(info + "退出运动功能")
                    self.log.debug(info + "Home键返回运动功能")
                app.device_home()
                app.saturn_inputclick("80", "160", "80", "160")
                self.log.debug(info + "点击Finish")
                app.saturn_inputclick("280", "280", "280", "280")
                self.log.debug(info + "点击Confirm")
                app.device_home()
                self.log.debug(info + "返回表盘页面成功")
            except:
                self.log.error(info + '进出运动功能在第N次运行失败：' + str(i))
                app.call_back_brandy(self.mac7, self.section, self.port, self.uuid)



if __name__ == '__main__':
    multiprocessings = []
    t1 = multiprocessing.Process(target=Testsmoke().smoke1)
    # t2 = multiprocessing.Process(target=Testsmoke().smoke2)
    # t3 = multiprocessing.Process(target=Testsmoke().smoke3)
    # t4 = multiprocessing.Process(target=Testsmoke().smoke4)
    # t5 = multiprocessing.Process(target=Testsmoke().smoke5)
    # t6 = multiprocessing.Process(target=Testsmoke().smoke6)
    # t7 = multiprocessing.Process(target=Testsmoke().smoke7)
    multiprocessings.append(t1)
    # multiprocessings.append(t2)
    # multiprocessings.append(t3)
    # multiprocessings.append(t4)
    # multiprocessings.append(t5)
    # multiprocessings.append(t6)
    # multiprocessings.append(t7)
    for t in multiprocessings:
        t.start()

