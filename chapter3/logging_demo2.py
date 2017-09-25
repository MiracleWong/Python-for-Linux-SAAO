#!/usr/local/bin/python
# -*- coding=utf-8 -*-
import logging

logging.basicConfig(
    filename='app.log',
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.DEBUG)

logging.debug('debug message')
logging.info('info message')
logging.error('error message')
logging.warn('warn message')
logging.critical('critical message')