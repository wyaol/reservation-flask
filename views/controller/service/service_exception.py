#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/21 18:38 
# @Author : wyao
# @File : service_exception.py
class GetOpenIdException(Exception):
    def __init__(self, msg=''):
        self.msg = msg
    def __str__(self):
        return self.msg


class NoTaskException(Exception):
    def __init__(self, msg=''):
        self.msg = msg
    def __str__(self):
        return self.msg