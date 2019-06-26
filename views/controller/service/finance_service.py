#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/24 15:16 
# @Author : wyao
# @File : finance_service.py
from .db import config
from .db.api import sql_client
from .service_exception import NoTaskException


class FinancService:

    def __init__(self):
        self.db_name = config.FINANCE_TABLE_NAME
        self.sql_client = sql_client

    def get_finance_id(self, open_id):
        data = self.sql_client.select(self.db_name, ['finance_id'], open_id=open_id)
        if len(data) == 0:
            return None
        return data[0][0]

    def register(self, finance_id, open_id):
        return self.sql_client.insert(self.db_name, finance_id=finance_id, open_id=open_id)

    def get_task(self, finance_id: str) -> str:
        """
        从当天任务队列中取出一个任务 返回信息msg
        :param finance_id: 财务人员id
        :return:
        """
        sql = 'SELECT task_id from task where to_days(reservate_time) = to_days(now()) and finance_id is null limit 1'
        # try:
        self.sql_client.cursor.execute(sql)
        res_data = self.sql_client.cursor.fetchall()
        if len(res_data) == 0:
            raise NoTaskException()
        print(res_data)
        sql2 = "update task set finance_id='%s', state='%s' where task_id='%s'"%(finance_id, '进行中', res_data[0][0])
        # print(sql2)
        self.sql_client.cursor.execute(sql2)
    # except Exception as e:
    #     self.sql_client.conn.rollback()  # 事务回滚
    #     msg = '事务处理失败 %s'%e
    # else:
        self.sql_client.conn.commit()  # 事务提交
        msg = '任务领取成功 %s'%self.sql_client.cursor.rowcount  # 关闭连接
        return msg

    def task_done(self, finance_id):
        return self.sql_client.update(config.TASK_TABLE_NAME, set={
            'state': '已完成'
        }, where={
            'finance_id': finance_id,
            'state': '进行中'
        })

    def has_task(self, finnance_id: str):
        res_date = self.sql_client.select(config.TASK_TABLE_NAME, ['*'], finance_id=finnance_id, state='进行中')
        return True if len(res_date) != 0 else False

finance_service = FinancService()