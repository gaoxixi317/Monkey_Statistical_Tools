#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:GAOXI
# datetime:2020/12/7 12:29
# software: PyCharm
from statistics_monkey_log.read_log3 import StaticMonkeyLog,CollectDdetail
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
