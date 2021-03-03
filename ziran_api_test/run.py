# -*- coding:utf-8 -*-
"""
测试启动程序
"""
# @Author   : 孜然v
# @Python   : 3.7.4

import os
import datetime
import unittest
import HtmlTestRunner

from ziran_api_test.public_modules.logger_module import LOGGER
from ziran_api_test.public_modules.email_module import MAIL_PUSH
from ziran_api_test.settings import TEST_LAUNCH_CONFIG, OUTPUT_REPORT_CONFIG, MAIL_CONFIG


class TestLaunch(object):

    def __init__(self, test_scripts_path, report_path, report_name_prefix, report_title,
                 execute_script_pattern='test_*.py'):
        """
        测试启动配置
        :param test_scripts_path: 测试脚本所在目录
        :param report_path: 输出报告路径
        :param report_name_prefix: 报告名称前缀
        :param report_title: 报告内容标题
        :param execute_script_pattern: 定义需要启动哪些测试脚本
        """
        self.test_scripts_path = test_scripts_path
        self.report_path = report_path
        self.report_name_prefix = report_name_prefix
        self.report_title = report_title
        self.execute_script_pattern = execute_script_pattern
        self.report_generate_path = None

    def run_test_case(self):
        """执行测试用例，并生成测试报告"""
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_scripts_path,
                                                       pattern=self.execute_script_pattern)
        runner = HtmlTestRunner.HTMLTestRunner(output=self.report_path, report_name=self.report_name_prefix,
                                               report_title=self.report_title)
        result = runner.run(discover)
        self.report_generate_path = list(result.report_files)  # 保存报告生成路径

    def mail_push(self):
        """将生成的测试报告推送到邮箱"""
        if MAIL_CONFIG['on_off'] == 'on':
            MAIL_PUSH.send_mail(sender=MAIL_CONFIG['sender'], receiver=MAIL_CONFIG['receiver'],
                                subject=MAIL_CONFIG['subject'],
                                body='<p> This is a test <p>', attachments=self.report_generate_path)

    def main(self):
        self.run_test_case()
        self.mail_push()


if __name__ == '__main__':
    test_launch = TestLaunch(TEST_LAUNCH_CONFIG['test_scripts_path'], OUTPUT_REPORT_CONFIG['report_path'],
                             OUTPUT_REPORT_CONFIG['report_name_prefix'], OUTPUT_REPORT_CONFIG['report_title'],
                             TEST_LAUNCH_CONFIG['execute_script_pattern'])
    test_launch.main()
