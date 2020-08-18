from flask import Flask
import logging
from logging.handlers import TimedRotatingFileHandler
import os


def create_logger():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    handler = TimedRotatingFileHandler('logs/fas.log', when='D')
    logging_format = logging.Formatter(
        '[%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - line:%(lineno)s]: %(message)s')
    handler.setFormatter(logging_format)
    return handler

app = Flask(__name__)
app.logger.addHandler(create_logger())

from yo import test1