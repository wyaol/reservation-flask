#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/21 20:52 
# @Author : wyao
# @File : reservate_views.py
import json
from flask import Blueprint, request, session
from .controller import control
from .controller.service import main_service


reservate_views = Blueprint('reservate_views', __name__)


@reservate_views.route('/reservate', methods = ['POST'])
def reservate():
    posts = request.form
    date = posts.get('calendar')
    time = posts.get('time')
    if control.reservate(date, time, session['id']) is not False:
        ret = {
            'success': True,
            'repeat': False,
            'msg': ''
        }
    else:
        ret = {
            'success': False,
            'repeat': True,
            'msg': '您已经预约过了'
        }
    return json.dumps(ret, ensure_ascii=False)

@reservate_views.route('/reservate_info', methods = ['GET'])
def reservate_info():
    posts = request.args
    date = posts.get('date')
    res_data = main_service.reservate_info(date)
    ret = {
        'success': True,
        'reservated': res_data
    }
    return json.dumps(ret, ensure_ascii=False)


@reservate_views.route('/reservate_teacher', methods = ['GET'])
def reservate_teacher():
    res_data = main_service.reservate_teacher(session['id'])
    ret = {
        'success': True,
        'reservated': res_data
    }
    return json.dumps(ret, ensure_ascii=False)


@reservate_views.route('/reservate_del', methods = ['POST'])
def reservate_del():
    posts = request.form
    reservate_time = posts.get('reservate_time')
    main_service.reservate_del(reservate_time, session['id'])
    ret = {
        'success': True,
    }
    return json.dumps(ret, ensure_ascii=False)


@reservate_views.route('/reservate_max', methods = ['POST'])
def reservate_max():
    posts = request.form
    reservate_max_value = posts.get('reservate_max')
    main_service.reservate_max(reservate_max_value)
    ret = {
        'success': True,
    }
    return json.dumps(ret, ensure_ascii=False)