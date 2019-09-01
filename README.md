#### 安装flask pymysql操作数据库 flask-login
python3 -m pip install flask  
python3 -m pip install pymysql  

#### 赋予operate.sh 权限
chmod 777 operate.sh  

#### 安装数据库
msyql 创建数据库 reservation  
chmod 777 install.sh  
./install.sh  

#### 配置发送邮件服务
修改views/controller/service/config.py 中EMAIL开头的信息
