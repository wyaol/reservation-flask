#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/25 11:11 
# @Author : wyao
# @File : work_views.py
import json
from flask import Blueprint, request, session
from .controller.service.finance_service import finance_service
from .controller import control
from .controller.service.service_exception import NoTaskException


work_views = Blueprint('work_views',__name__)


@work_views.route('/task_done', methods=['POST'])
def task_done():
    if finance_service.has_task(session['id']) is True:
        finance_service.task_done(session['id'])
    return json.dumps({
        'success': True
    }, ensure_ascii=False)


@work_views.route('/get_task', methods=['GET'])
def get_task():
    try:
        msg = control.get_task(session['id'])
        return json.dumps({
            'success': True,
            'task_empty': False,
            'msg': msg
        }, ensure_ascii=False)
    except NoTaskException:
        return json.dumps({
            'success': True,
            'task_empty': True,
            'msg': '所有任务已完成， 当前无任务'
        }, ensure_ascii=False)


@work_views.route('/reservate_info', methods=['POST'])
def reservate_info():
    posts = request.form
    date = posts.get('date')
    time = posts.get('time')
    res_data = control.reservate_info(date, time)
    return json.dumps({
        'success': True,
        'task_empty': False,
        'reservate_info': res_data
    }, ensure_ascii=False)