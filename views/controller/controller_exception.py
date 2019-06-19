#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/19 11:08 
# @Author : wyao
# @File : controller_exception.py


class LoginFailException(Exception):

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return str(self.msg)