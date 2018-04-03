#!/usr/bin/env python
#-*- coding: GBK -*-
import os
import sys


# Django 常用命令
# python manage.py runserver 启动服务器
# python manage.py inspectdb > web/models.py 从数据库逆向生成models
# python manage.py syncdb 将models生成数据库表




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
