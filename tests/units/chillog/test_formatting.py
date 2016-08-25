import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../../../')

from chillog.logger import Chillog


class TestFormatting(unittest.TestCase):
    def setUp(self):
        super(TestFormatting, self).setUp()
        self.host = 'TEST_MODULE'
        self.logger = Chillog(self.host)

    def test_build_json_log_info_success(self):
        message = 'test formatting'
        json_log = self.logger.build_json_log(log_level=self.logger.LOG_INFO,
                                              short_msg=message,
                                              key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_warning_success(self):
        message = 'test formatting'
        json_log = self.logger.build_json_log(log_level=self.logger.LOG_WARNING,
                                              short_msg=message,
                                              key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['level'], self.logger.LOG_WARNING)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_alert_success(self):
        message = 'test formatting'
        json_log = self.logger.build_json_log(log_level=self.logger.LOG_ALERT,
                                              short_msg=message,
                                              key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['level'], self.logger.LOG_ALERT)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_critical_success(self):
        message = 'test formatting'
        json_log = self.logger.build_json_log(log_level=self.logger.LOG_CRITICAL,
                                              short_msg=message,
                                              key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['level'], self.logger.LOG_CRITICAL)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_info_with_dict_success(self):
        message = 'test formatting'
        additional_dict = {
            'key': 'value'
        }
        json_log = self.logger.build_json_log(log_level=self.logger.LOG_INFO,
                                              short_msg=message,
                                              **additional_dict)

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.host)
        self.assertEqual(json_log['level'], self.logger.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_wrong_log_level(self):
        message = 'test formatting'
        json_log = self.logger.build_json_log(log_level='WRONG',
                                              short_msg=message,
                                              key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['level'], self.logger.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')
