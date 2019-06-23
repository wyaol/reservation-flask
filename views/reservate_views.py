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
    control.reservate(date, time)
    ret = {
        'success': True,
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
    print(res_data)
    return json.dumps(ret, ensure_ascii=False)