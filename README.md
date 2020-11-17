Django学习

## 一、开发环境

### python

安装python2.7

按照python3.6.4

```
yum install sqlite-devel
wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
tar -xvJf  Python-3.6.4.tar.xz
cd Python-3.6.4/
# 编译
./configure prefix=/usr/local/python3
make && make install

#添加软链到执行目录下/usr/bin

ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```


### PIP

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py


sudo apt-get install python-pip
sudo apt-get install python3-pip
```



### virtualenv

```
pip install virtualenv
```

### 一套独立的Python运行环境

**GP1为Python2.7.5 GP2为Python3.6.4**

```
virtualenv GP1 -p /usr/bin/python


source /opt/Django_test/GP1/bin/activate

# 退出虚拟环境
deactivate
```



### Django

```
source /opt/Django_test/GP2/bin/activate


 pip install django==1.11.7
```

## 二、Django项目搭建

```
django-admin startproject demoDjango
```


新建demo1

```
python manage.py startapp demo1
```

```
python manage.py runserver 0.0.0.0:8000
```


修改创建项目时生成的setting.py文件

将

```
ALLOWED_HOSTS = []
```

改为

```
ALLOWED_HOSTS = ['*']
```
