import os
import logging
import time
from logging.handlers import RotatingFileHandler


def make_dir(make_dir_path):
    path = make_dir_path.strip()
    # print(path)
    if not os.path.exists(path):
        os.makedirs(path)


def getLogHandler():
    # 日志地址
    log_dir_name = "Logs"
    log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    log_file_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
    make_dir(log_file_folder)
    log_file_str = log_file_folder + os.sep + log_file_name

    logging.basicConfig(level=logging.INFO)
    file_log_handler = RotatingFileHandler(log_file_str, maxBytes=1024 * 1024, backupCount=10, encoding='UTF-8')
    # 设置日志的格式                   发生时间    日志等级     日志信息文件名      函数名          行数        日志信息
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s '
                                  '- %(funcName)s - %(lineno)s - %(message)s')
    file_log_handler.setFormatter(formatter)

    return file_log_handler
