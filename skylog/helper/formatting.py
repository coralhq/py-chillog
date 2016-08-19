import time

from skylog.helper import constants


def _get_current_timestamp():
    return int(round(time.time() * 1000))


def _add_param_to_dict(dict_to_add, **kwargs):
    for key, value in kwargs.items():
        key = '_' + str(key)
        dict_to_add[key] = value

    return dict_to_add


def build_json_log(log_level, msg, **kwargs):
    expected_level = [constants.LOG_INFO, constants.LOG_ALERT, constants.LOG_CRITICAL, constants.LOG_WARNING]

    if log_level not in expected_level:
        log_level = constants.LOG_INFO

    json_log = {
        'version': constants.LOG_MESSAGE_VERSION,
        'host': constants.HOST,
        'message': msg,
        'timestamp': _get_current_timestamp(),
        'level': log_level
    }

    json_log = _add_param_to_dict(json_log, **kwargs)

    return json_log
