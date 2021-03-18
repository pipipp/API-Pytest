# -*- coding:utf-8 -*-
"""
Allure报告模块
"""

import allure


def add_common_report(case, http, expected):
    """
    添加常用报告信息
    :param case: 测试用例名称
    :param http: 请求对象
    :param expected: 预期结果
    :return:
    """
    with allure.step('测试用例名称'):
        allure.attach(case)

    with allure.step('请求对象'):
        allure.attach(http['path'], 'path')
        allure.attach(http['method'], 'method')
        with allure.step('headers'):
            for key, value in http['headers'].itmes():
                allure.attach(value, key)
        with allure.step('params'):
            for key, value in http['params'].itmes():
                allure.attach(value, key)

    with allure.step('预期结果'):
        for key, value in expected['response'].itmes():
            allure.attach(value, key)
