import pymysql
from . import config


class SQL:

    def __init__(self, host=config.HOST, user=config.USER, password=config.PASSWORD,
                 database=config.DATABASE, charset=config.CHARSET, read_timeout=config.READ_TIMEOUT,
                 write_timeout=config.WRITE_TIMEOUT):
        # 连接database
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database,
                                    charset=charset, read_timeout=read_timeout, write_timeout=write_timeout)
        # 得到一个可以执行SQL语句的光标对象
        self.cursor = self.conn.cursor()

    def insert(self, table_name, **kwargs):
        self.conn.ping(reconnect=True)
        sql = 'insert into %s (%s) values (%s)'%(table_name,
                                                 SQL.keys2str(list(kwargs.keys())),
                                                 SQL.values2str(list(kwargs.values())))
        self.cursor.execute(sql)
        self.conn.commit()

    def delete(self, table_name, **kwargs):
        self.conn.ping(reconnect=True)
        sql = 'delete from %s where %s'%(table_name, SQL.dict2str(kwargs))
        self.cursor.execute(sql)
        self.conn.commit()

    def update(self, table_name: str, set: dict, where: dict):
        self.conn.ping(reconnect=True)
        sql = 'update %s set %s where %s'%(table_name, SQL.dict2str(set, ', '), SQL.dict2str(where))
        self.cursor.execute(sql)
        self.conn.commit()

    def select(self, table_name: str, argvs: list, **kwargs):
        """
        简单查询数据库，返回所有记录
        :param table_name: 表名
        :param argvs: 选择的字段
        :param kwargs: where限定条件
        :return: 记录 二维元组
        """
        self.conn.ping(reconnect=True)
        sql = 'select %s from %s where %s'%(SQL.keys2str(argvs), table_name, SQL.dict2str(kwargs))
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    @staticmethod
    def keys2str(keys: list, connector: str=', '):
        return connector.join(keys)

    @staticmethod
    def values2str(keys: list):
        for i in range(len(keys)):
            keys[i] = SQL.add_quotes(keys[i])
        return ', '.join(keys)

    @staticmethod
    def dict2str(kwargs: dict, connector: str=' and '):
        """
        格式化字典为字符串
        :param kwargs: 传入的字典
        :param connector: 最终连接符
        :return:
        """
        items = kwargs.items()
        items_list = []
        for item in items:
            item = list(item)
            item[1] = SQL.add_quotes(item[1])
            items_list.append('='.join(item))
        return connector.join(items_list)

    @staticmethod
    def add_quotes(field):
        """
        给str类型字段加上单引号
        :param field: 字段 未知类型
        :return:
        """
        if isinstance(field, str):
            return "'%s'"%field

    def close(self):
        """
        数据库直到进程关闭才断开连接
        :return:
        """
        pass


sql_client = SQL()