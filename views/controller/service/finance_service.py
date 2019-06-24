#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/24 15:16 
# @Author : wyao
# @File : finance_service.py
from .db import config
from .db.api import sql_client


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

    def get_task(self, finance_id):
        sql = 'SELECT task_id from task where to_days(reservate_time) = to_days(now()) and finance_id is null limit 1'
        try:
            self.sql_client.cursor.execute(sql)
            res_data = self.sql_client.cursor.fetchall()
            print(res_data)
            sql2 = "update task set finance_id='%s', state='%s' where task_id='%s'"%(finance_id, '进行中', res_data[0][0])
            print(sql2)
            self.sql_client.cursor.execute(sql2)
        except Exception as e:
            self.sql_client.conn.rollback()  # 事务回滚
            print('事务处理失败', e)
        else:
            self.sql_client.conn.commit()  # 事务提交
            print('事务处理成功', self.sql_client.cursor.rowcount)  # 关闭连接
        return

finance_service = FinancService()