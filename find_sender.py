#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 正则匹配
import fileinput, re

pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:
        print(m.group(1))

# 命令行find_sender.py message.eml运行
