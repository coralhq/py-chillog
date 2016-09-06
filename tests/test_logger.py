import os
import socket
import unittest
from chillog.logger import Chillog


class TestLogger(unittest.TestCase):
    def setUp(self):
        super(TestLogger, self).setUp()
        self.hostname = 'TEST_HOST'
        self.service_name = 'TEST_SERVICE'
        self.logger = Chillog(service_name=self.service_name,
                              hostname=self.hostname)

    def test_build_json_log_info_with_default_config(self):
        os.environ["SERVICE_NAME"] = "TEST_SERVICE"
        default_logger = Chillog()
        message = 'test formatting'
        json_log = default_logger.build_log_message(log_level=self.logger.LOG_INFO,
                                                    short_message=message,
                                                    key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], socket.gethostname())
        self.assertEqual(json_log['service'], os.environ.get("SERVICE_NAME"))
        self.assertEqual(json_log['level'], self.logger.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')

        del os.environ["SERVICE_NAME"]
        os.unsetenv("SERVICE_NAME")

    def test_build_json_log_info_with_default_config_without_os_eviron(self):
        default_logger = Chillog()
        message = 'test formatting'
        json_log = default_logger.build_log_message(log_level=self.logger.LOG_INFO,
                                                    short_message=message,
                                                    key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], socket.gethostname())
        self.assertEqual(json_log['service'], None)
        self.assertEqual(json_log['level'], self.logger.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_info_success(self):
        message = 'test formatting'
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_INFO,
                                                 short_message=message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_warning_success(self):
        message = 'test formatting'
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_WARNING,
                                                 short_message=message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_WARNING)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_alert_success(self):
        message = 'test formatting'
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_ALERT,
                                                 short_message=message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_ALERT)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_critical_success(self):
        message = 'test formatting'
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_CRITICAL,
                                                 short_message=message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_CRITICAL)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_debug_success(self):
        message = 'test formatting'
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_DEBUG,
                                                 short_message=message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_DEBUG)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_error_success(self):
        message = 'test formatting'
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_ERROR,
                                                 short_message=message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_ERROR)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_notice_success(self):
        message = 'test formatting'
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_NOTICE,
                                                 short_message=message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_NOTICE)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_info_with_dict_success(self):
        message = 'test formatting'
        additional_dict = {
            'key': 'value'
        }
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_INFO,
                                                 short_message=message,
                                                 **additional_dict)

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_wrong_log_level(self):
        message = 'test formatting'
        json_log = self.logger.build_log_message(log_level='WRONG',
                                                 short_message=message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')

    def test_build_json_log_with_full_msg(self):
        message = 'test formatting'
        long_message = 'test looooooooong formatting'
        json_log = self.logger.build_log_message(log_level=self.logger.LOG_INFO,
                                                 short_message=message,
                                                 full_message=long_message,
                                                 key='value')

        self.assertIsInstance(json_log, dict)
        self.assertEqual(json_log['version'], self.logger.LOG_MESSAGE_VERSION)
        self.assertEqual(json_log['short_message'], message)
        self.assertEqual(json_log['full_message'], long_message)
        self.assertEqual(json_log['host'], self.hostname)
        self.assertEqual(json_log['service'], self.service_name)
        self.assertEqual(json_log['level'], self.logger.LOG_INFO)
        self.assertEqual(json_log['_key'], 'value')
