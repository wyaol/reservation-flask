#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/24 15:16 
# @Author : wyao
# @File : finance_service.py
from .db import config
from .db.api import SQL
from .service_exception import NoTaskException


class FinancService:

    def __init__(self):
        self.db_name = config.FINANCE_TABLE_NAME

    def get_finance_id(self, open_id):
        data = SQL().select(self.db_name, ['finance_id'], open_id=open_id)
        if len(data) == 0:
            return None
        return data[0][0]

    def register(self, finance_id, open_id):
        return SQL().insert(self.db_name, finance_id=finance_id, open_id=open_id)

    def get_task(self, finance_id: str) -> str:
        """
        从当天任务队列中取出一个任务 返回教师id
        :param finance_id: 财务人员id
        :return: 返回教师id
        """
        sql_client = SQL()
        sql = 'SELECT task_id, teacher_id ' \
              'from task ' \
              'where to_days(reservate_time) = to_days(now()) and finance_id is null ' \
              'order by reservate_time ASC ' \
              'limit 1'
        # try:
        sql_client.cursor.execute(sql)
        res_data = sql_client.cursor.fetchall()
        if len(res_data) == 0:
            raise NoTaskException()
        print(res_data)
        sql2 = "update task set finance_id='%s', state='%s' where task_id='%s'"%(finance_id, '进行中', res_data[0][0])
        # print(sql2)
        sql_client.cursor.execute(sql2)
    # except Exception as e:
    #     self.sql_client.conn.rollback()  # 事务回滚
    #     msg = '事务处理失败 %s'%e
    # else:
        sql_client.conn.commit()  # 事务提交
        sql_client.cursor.close()
        sql_client.conn.close()
        return res_data[0][1]

    def task_done(self, finance_id):
        SQL().update(config.TASK_TABLE_NAME, set={
            'state': '已完成'
        }, where={
            'finance_id': finance_id,
            'state': '进行中'
        })

    def has_task(self, finnance_id: str):
        res_date = SQL().select(config.TASK_TABLE_NAME, ['*'], finance_id=finnance_id, state='进行中')
        return True if len(res_date) != 0 else False

    def reservate_info(self, date, time):
        sql_client = SQL()
        sql = "select name, reservate_time, state " \
              "from task left join teacher " \
              "on task.teacher_id = teacher.teacher_id " \
              "where reservate_time='%s %s'"%(date, time)
        sql_client.cursor.execute(sql)
        res_date = sql_client.cursor.fetchall()
        return [{'name': e[0], 'reservate_time': e[1].strftime('%Y-%m-%d %H:%M:%S'), 'state': e[2]} for e in res_date]

finance_service = FinancService()