#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/21 15:09 
# @Author : wyao
# @File : identity_control_view.py
import json
from flask import Blueprint, request, session
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
                'is_register': True,
                'identity': session['identity']
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
        control.register(identity, id, session['open_id'])
        ret = {
            'success': True,
        }
    except IdentityNotExistException as e:
        ret = {
            'success': False,
            'msg': str(e)
        }
    return json.dumps(ret, ensure_ascii=False)


@identity_control_views.route('/set_info', methods=['POST'])
def set_info():
    posts = request.form
    name = posts.get('name')
    sex = posts.get('sex')
    phone_number = posts.get('phone_number')
    try:
        ret = control.set_info(session['id'], name, sex, phone_number)
        ret = {
            'success': True,
            'msg': str(ret)
        }
    except IdentityNotExistException as e:
        ret = {
            'success': False,
            'msg': str(e)
        }
    return json.dumps(ret, ensure_ascii=False)


@identity_control_views.route('/get_info', methods=['GET'])
def get_info():
    try:
        ret = control.get_info(session['id'], session['identity'])
        ret = {
            'success': True,
            'teacher_info': ret
        }
    except IdentityNotExistException as e:
        ret = {
            'success': False,
            'msg': str(e)
        }
    return json.dumps(ret, ensure_ascii=False)