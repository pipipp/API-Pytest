"""
项目环境配置
"""
# -*- coding:utf-8 -*-
import os
import datetime


# 项目名称
PROJECT_NAME = 'hrms'

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 各模块目录
MODULE_DIR = {
    'logs_dir': os.path.join(BASE_DIR, 'logs'),  # 日志模块目录
    'test_file_dir': os.path.join(BASE_DIR, 'test_case_file'),  # 测试用例文件目录
    'test_scripts_dir': os.path.join(BASE_DIR, 'test_case_scripts'),  # 测试用例脚本目录
    'reports_dir': os.path.join(BASE_DIR, 'reports'),  # 生成报告目录
}

# 日志文件配置
LOG_CONFIG = {
    'formatter': '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    'console_output_level': 'DEBUG',
    'file_output_level': 'DEBUG',
    'log_file_name': os.path.join(MODULE_DIR['logs_dir'], f'{PROJECT_NAME}.log'),
    'backup_count': 5,
}

# 邮件推送配置
MAIL_CONFIG = {
    'on_off': 'off',
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 25,
    'smtp_user': 'evan.liu@qq.com',
    'smtp_password': '',
    'sender': 'evan.liu@qq.com',
    'receiver': 'ziran.pipi@qq.com',
    'subject': '接口自动化测试报告',
}

# 输出报告配置
OUTPUT_REPORT_CONFIG = {
    'report_path': os.path.join(MODULE_DIR['reports_dir'], datetime.datetime.now().strftime('%Y-%m-%d')),
    'report_name_prefix': 'hrms',
    'report_title': '自动化测试报告',
}

# 测试启动配置
TEST_LAUNCH_CONFIG = {
    'test_scripts_path': MODULE_DIR['test_scripts_dir'],
    'execute_script_pattern': 'test_*.py',
}
