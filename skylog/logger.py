from skylog.helper.formatting import build_json_log

from skylog.helper import constants


def skylog_init(app_name):
    constants.HOST = app_name


def info(msg, **kwargs):
    json_log = build_json_log(log_level=constants.LOG_INFO,
                              msg=msg,
                              **kwargs)
    print json_log


def alert(msg, **kwargs):
    json_log = build_json_log(log_level=constants.LOG_ALERT,
                              msg=msg,
                              **kwargs)
    print json_log


def warning(msg, **kwargs):
    json_log = build_json_log(log_level=constants.LOG_WARNING,
                              msg=msg,
                              **kwargs)
    print json_log


def critical(msg, **kwargs):
    json_log = build_json_log(log_level=constants.LOG_CRITICAL,
                              msg=msg,
                              **kwargs)
    print json_log
