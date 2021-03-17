# -*- coding:utf-8 -*-
import os
import pytest
import requests

from pytest_project.utils.common import get_yaml_test_data
from pytest_project.config.settings import MODULE_DIR

# 获取测试数据
cases, params = get_yaml_test_data(os.path.join(MODULE_DIR['test_data_dir'], 'test_proxy.yaml'))


class TestProxy(object):

    @pytest.fixture(scope='function')
    def preparation(self):
        """测试的准备与收尾"""
        print('在数据库中准备测试数据')
        test_data = '在数据库中准备测试数据'
        yield test_data
        print('清理测试数据')

    @pytest.mark.parametrize('case,http,expected', params, ids=cases)
    def test_proxy(self, env, case, http, expected):
        r = requests.request(http['method'],
                             url=env['host'] + http['path'],
                             headers=http['headers'],
                             params=http['params'])
        resp = r.json()

        assert resp['status'] == expected['response']['status']
        assert resp['message'] == expected['response']['message']
        assert bool(resp['data']) == expected['response']['data']
