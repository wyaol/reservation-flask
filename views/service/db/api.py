import pymysql
from . import config


class SQL:

    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象 保证进程和远程数据库不会建立多余的链接
        if not hasattr(cls, 'instance'):
            cls.instance = super(SQL, cls).__new__(cls)
        return cls.instance

    def __init__(self, host=config.HOST, user=config.USER, password=config.PASSWORD, database=config.DATABASE, charset=config.CHARSET):
        # 连接database
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database)
        # 得到一个可以执行SQL语句的光标对象
        self.cursor = self.conn.cursor()

    def insert(self, table_name, *argvs, **kwargs):
        sql = 'insert into %s (%s) values (%s)'%(table_name,
                                                 SQL.keys2str(list(kwargs.keys())),
                                                 SQL.values2str(list(kwargs.values())))
        self.cursor.execute(sql)
        self.conn.commit()

    @staticmethod
    def keys2str(keys: list):
        return ', '.join(keys)

    @staticmethod
    def values2str(keys: list):
        for i in range(len(keys)):
            if isinstance(keys[i], str):
                keys[i] = "'%s'" % keys[i]
        return ', '.join(keys)

    def close(self):
        """
        数据库直到进程关闭才断开连接
        :return:
        """
        pass


sql = SQL().instance