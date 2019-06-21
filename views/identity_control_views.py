#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/21 15:09 
# @Author : wyao
# @File : identity_control_view.py
import json
from flask import Blueprint, request
from .controller import control
from .controller.controller_exception import IdentityNotExistException
from .controller.service.service_exception import GetOpenIdException


identity_control_views = Blueprint('identity_control_views',__name__)


@identity_control_views.route('/login')
def login():
    get_args = request.args
    code = get_args.get('code')
    try:
        if control.login(code):
            ret = {
                'success': True,
                'is_register': True
            }
        else:
            ret = {
                'success': True,
                'is_register': False,
                'msg': '该用户未绑定'
            }
    except GetOpenIdException as e:
        ret = {
            'success': False,
            'msg': str(e)
        }
    return json.dumps(ret, ensure_ascii=False)


@identity_control_views.route('/register', methods=['POST'])
def register():
    posts = request.form
    identity = posts.get('identity')
    id = posts.get('id')
    try:
        control.register(identity, id)
        ret = {
            'success': True,
        }
    except IdentityNotExistException as e:
        ret = {
            'success': False,
            'msg': str(e)
        }
    return json.dumps(ret, ensure_ascii=False)