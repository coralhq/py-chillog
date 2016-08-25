import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../../../')

from skylog.logger import skylog_init
from skylog.helper.constants import *
from skylog.helper.formatting import *


class TestFormatting(unittest.TestCase):

    def setUp(self):
        super(TestFormatting, self).setUp()
        self.host = 'TEST_MODULE'
        skylog_init(self.host)

    def test_build_json_log_info_success(self):
        message = 'test formatting'
        json_log = build_json_log(log_level=LOG_INFO,
                                  msg=message,
                                  key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_warning_success(self):
        message = 'test formatting'
        json_log = build_json_log(log_level=constants.LOG_WARNING,
                                  msg=message,
                                  key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], constants.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['level'], constants.LOG_WARNING)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_alert_success(self):
        message = 'test formatting'
        json_log = build_json_log(log_level=constants.LOG_ALERT,
                                  msg=message,
                                  key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], constants.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['level'], constants.LOG_ALERT)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_critical_success(self):
        message = 'test formatting'
        json_log = build_json_log(log_level=constants.LOG_CRITICAL,
                                  msg=message,
                                  key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], constants.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['level'], constants.LOG_CRITICAL)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_info_with_dict_success(self):
        message = 'test formatting'
        additional_dict = {
            'key': 'value'
        }
        json_log = build_json_log(log_level=constants.LOG_INFO,
                                  msg=message,
                                  **additional_dict)

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], constants.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['level'], constants.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_wrong_log_level(self):
        message = 'test formatting'
        json_log = build_json_log(log_level='WRONG',
                                  msg=message,
                                  key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], constants.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['message'], message)
        self.assertEqual(json_log['level'], constants.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')
