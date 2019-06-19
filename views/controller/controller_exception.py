#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/19 11:08 
# @Author : wyao
# @File : controller_exception.py


class LoginFailException(Exception):

    def __int__(self, msg):
        self.msg = msg
        pass

    def __str__(self):
        return str(self.msg)