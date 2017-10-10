# -*- coding: utf-8 -*-
"""

@file: setting.py

@time: 2017/8/29 14:25

@desc:

"""
import os
import sys
import platform
import configparser

##
if platform.system() == 'Windows':
    root_dir = '/'.join(os.path.realpath(__file__).split('\\')[:-1])
else:
    root_dir = '/'.join(os.path.realpath(__file__).split('/')[:-1])
sys.path.append(root_dir)
logLevel = 2
logFile = os.path.join(root_dir, 'logs')
cfg = configparser.ConfigParser()
print(root_dir)
# CONFIG_FILE = os.path.join(root_dir, 'conf/system.cfg')
# try:
#     with open(CONFIG_FILE, 'r') as cfg_file:
#         cfg.readfp(cfg_file)
#         es_ip = cfg.get('info', 'ES_ADD')
# except FileNotFoundError as err:
#     print(err)
