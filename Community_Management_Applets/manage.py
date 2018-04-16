#!/usr/bin/env python
#-*- coding: GBK -*-
import os
import sys


# Django 常用命令
# python manage.py runserver 启动本地调试服务器
# python manage.py inspectdb > web/models.py 从数据库逆向生成models
# python manage.py runserver 0.0.0.0:8000 ,可使其他电脑通过http://[本机IP]:8000访问



if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Community_Management_Applets.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and " 
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
