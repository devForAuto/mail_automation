# -*- coding: utf-8 -*-
from __future__ import print_function

"""

@file: base_conf.py

@time: 2017/8/19 17:30

@desc:读取配置文件

"""

import configparser
import os
import sys
import platform

class ConSys(object):
    def cons(self):
        if platform.system() == 'Windows':
            root_dir = '/'.join(os.path.realpath(__file__).split('\\')[:-3])
        else:
            root_dir = '/'.join(os.path.realpath(__file__).split('/')[:-1])
        sys.path.append(root_dir)
        print(root_dir)
        config_file = os.path.join(root_dir, 'config/system.cfg')
        config = configparser.ConfigParser()
        # config_file = './config/system.cfg'
        with open(config_file, 'r') as cfg_file:
            config.readfp(cfg_file)
            name = config.get('info', 'host')
        return name
