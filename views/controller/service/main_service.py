import json
import requests
import smtplib
from email.mime.text import MIMEText   # 导入模块
from .db.api import SQL
from .db import config
from functools import wraps
from flask import session
from .service_exception import GetOpenIdException
from . import config as service_config


def login_require(func):
    @wraps(func)
    def wrapper(*argvs, **kwargs):
        if 'id' not in session:
            return json.dumps({
                'success': False,
                'redict': True,
                'msg': '您没有访问权限， 请登录'
            })
        return func(*argvs, **kwargs)
    return  wrapper


def register(identity, id):
    if identity == 'teacher':
        SQL().insert(config.TEACHER_TABLE_NAME, teacher_id=id)
    else:
        print('identity not define')


def get_open_id(code):
    url = config.GET_OPEN_ID_URL % (config.APPID, config.SECRET, code)
    page = requests.get(url)
    json_str = page.text
    try:
        return eval(json_str)['openid']
    except Exception as e:
        raise GetOpenIdException('get open_id error return value is %s, system return is %s'%(json_str, str(e)))


def reservate(date: str, time: str, id):
    return SQL().insert(config.TASK_TABLE_NAME, reservate_time='%s %s'%(date, time),
                              teacher_id=id
                             )


def is_reservated(date, time):
    res_data = SQL().select(config.TASK_TABLE_NAME, ['*'], teacher_id=session['id'],
                      reservate_time='%s %s'%(date, time))
    return True if len(res_data) != 0 else False


def reservate_info(date: str):
    """
    查询某个日期
    :param date: 某个日期
    :return: list 数组 存储每条记录字典
    """
    sql_client = SQL()
    sql_client.conn.ping(reconnect=True)
    sql_str = "select reservate_time, count(*) reservated_num " \
              "from task " \
              "where to_days(reservate_time) = to_days('%s') " \
              "group by reservate_time"%date
    sql_client.cursor.execute(sql_str)
    res_data = sql_client.cursor.fetchall()
    res_list = [{'reservate_time': e[0].strftime('%Y-%m-%d %H:%M:%S'), 'reservate_forbid':True }
            if int(e[1]) >= config.MAX_TASK_NUM else None for e in res_data]
    return list(filter(None, res_list))


def reservate_teacher(id):
    teacher_id = id
    sql_client = SQL()
    res_data = sql_client.select(config.TASK_TABLE_NAME, ['reservate_time', 'state'], teacher_id=teacher_id)
    return [{'reservate_time': e[0].strftime('%Y-%m-%d %H:%M:%S'), 'state': e[1]} for e in res_data]


def send_emil(recv: str, content: str,
               title=service_config.EMAIL_TITLE, username=service_config.EMAIL_USERNAME, passwd=service_config.EMAIL_PASSWORD,
               mail_host=service_config.EMAIL_HOST, port=service_config.EMAIL_PORT):
    """
    :param recv: 收件者邮箱地址 例如123456@qq.com
    :param content: 邮件文本内容
    :param title:
    :param username:
    :param passwd:
    :param mail_host:
    :param port:
    :return:
    """
    msg = MIMEText(content)  # 邮件内容
    msg['Subject'] = title
    msg['From'] = username
    msg['To'] = recv
    smtp = smtplib.SMTP_SSL(mail_host, port=port)  # 定义邮箱服务类型
    smtp.login(username, passwd)  # 登录邮箱
    smtp.sendmail(username, recv, msg.as_string())  # 发送邮件
    smtp.quit()
    return True


def reservate_del(reservate_time: str, teacher_id: str):
    sql_client = SQL()
    sql_client.delete(config.TASK_TABLE_NAME, teacher_id=teacher_id, reservate_time=reservate_time)