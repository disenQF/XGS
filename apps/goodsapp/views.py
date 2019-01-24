from django.shortcuts import render

# Create your views here.
from goodsapp.models import Goods

from base import rank

def show(request, id):
    rank.add_week_rank(id)

    goods = Goods.objects.get(pk=id)
    return render(request, 'goods/show.html', locals())