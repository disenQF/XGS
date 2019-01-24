import xadmin
# Register your models here.
from django.views.generic import ListView

from activeapp.models import Active


@xadmin.sites.register(Active)
class ActiveAdmin(object):
    list_display = ('title', 'start_time', 'end_time', 'active_type_name')
