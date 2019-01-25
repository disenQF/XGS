"""XGS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render
from django.urls import path, include
import xadmin as admin

from goodsapp.models import Category, Goods
from base import rank


def to_index(request):
    categorys = Category.objects.filter(level=1)
    goods_list = Goods.objects.all()

    week_rank = rank.top_week_rank()
    return render(request, 'index.html', locals())


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userapp.urls')),
    path('goods/', include('goodsapp.urls')),
    path('search/', include('haystack.urls')),
    path('', to_index)
]
