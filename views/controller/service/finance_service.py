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


finance_service = FinancService()