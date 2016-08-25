import socket
import time


class Chillog:
    LOG_MESSAGE_VERSION = 1

    LOG_ALERT = 1
    LOG_CRITICAL = 2
    LOG_ERROR = 3
    LOG_WARNING = 4
    LOG_NOTICE = 5
    LOG_INFO = 6
    LOG_DEBUG = 7

    def __init__(self, hostname=None):
        self.__hostname = hostname if hostname else socket.gethostname()

    @staticmethod
    def __get_current_timestamp():
        return int(round(time.time() * 1000))

    @staticmethod
    def __add_param_to_dict(dict_to_add, **kwargs):
        for key, value in kwargs.items():
            key = '_' + str(key)
            dict_to_add[key] = value

        return dict_to_add

    def build_json_log(self, log_level, short_msg, **kwargs):
        expected_level = [
            self.LOG_ALERT,
            self.LOG_CRITICAL,
            self.LOG_ERROR,
            self.LOG_WARNING,
            self.LOG_NOTICE,
            self.LOG_INFO,
            self.LOG_DEBUG
        ]

        if log_level not in expected_level:
            log_level = self.LOG_INFO

        json_log = {
            'version': self.LOG_MESSAGE_VERSION,
            'host': self.__hostname,
            'short_message': short_msg,
            'full_message': short_msg,
            'timestamp': self.__get_current_timestamp(),
            'level': log_level
        }

        json_log = self.__add_param_to_dict(json_log, **kwargs)

        return json_log

    def info(self, msg, **kwargs):  # pragma: no cover
        json_log = self.build_json_log(log_level=self.LOG_INFO,
                                       short_msg=msg,
                                       **kwargs)
        print json_log

    def alert(self, msg, **kwargs):  # pragma: no cover
        json_log = self.build_json_log(log_level=self.LOG_ALERT,
                                       short_msg=msg,
                                       **kwargs)
        print json_log

    def warning(self, msg, **kwargs):  # pragma: no cover
        json_log = self.build_json_log(log_level=self.LOG_WARNING,
                                       short_msg=msg,
                                       **kwargs)
        print json_log

    def critical(self, msg, **kwargs):  # pragma: no cover
        json_log = self.build_json_log(log_level=self.LOG_CRITICAL,
                                       short_msg=msg,
                                       **kwargs)
        print json_log

    def debug(self, msg, **kwargs):  # pragma: no cover
        json_log = self.build_json_log(log_level=self.LOG_DEBUG,
                                       short_msg=msg,
                                       **kwargs)
        print json_log
