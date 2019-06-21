#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/21 20:52 
# @Author : wyao
# @File : reservate_views.py
import json
from flask import Blueprint, request
from .controller.service import main_service


reservate_views = Blueprint('reservate_views', __name__)


@reservate_views.route('/reservate', methods = ['POST'])
def reservate():
    posts = request.form
    date = posts.get('calendar')
    time = posts.get('time')
    main_service.register(date, time)
    ret = {
        'success': True,
    }
    return json.dumps(ret, ensure_ascii=False)