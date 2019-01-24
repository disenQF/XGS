from __future__ import absolute_import
import os

from celery import Celery

from XGS import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'XGS.settings')

app = Celery(__name__)
app.config_from_object('django.conf:settings')

# 从所有已安装的app模块中查找tasks.py中任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)