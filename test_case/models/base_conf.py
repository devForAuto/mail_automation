# -*- coding: utf-8 -*-
from __future__ import print_function

"""

@file: base_conf.py

@time: 2017/8/19 17:30

@desc:读取配置文件

"""

import sys
import configparser


class ConSys(object):
    def cons(self):
        config = configparser.ConfigParser()
        config_file = 'F:/mail_automation/config/system.cfg'
        with open(config_file, 'r') as cfg_file:
            config.readfp(cfg_file)
            name = config.get('info', 'host')
        return name
