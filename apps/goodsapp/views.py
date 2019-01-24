from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from goodsapp.models import Goods

from base import rank, rd
from goodsapp.tasks import qbuy_task

def show(request, id):
    rank.add_week_rank(id)

    goods = Goods.objects.get(pk=id)
    return render(request, 'goods/show.html', locals())


def qbuy(req, id):
    # 验证用户是否已登录
    login_user = req.session.get('login_user')
    if not login_user:
        msg = {'code': 100, 'msg': '用户未登录'}
    else:
        # 判断是否已抢完
        user_id = login_user.get('user_id')
        if rd.hexists('qbuy', user_id):
            msg = {'code': 201, 'msg': '每一位用户每天只能抢一次'}
        else:
            if rd.hlen('qbuy') >= 5:
                msg = {'code': 202,
                       'msg': '今日已抢完'}
            else:
                msg = {'code': 203,
                       'msg': '正在抢'}
                qbuy_task.delay(user_id, id)

    return JsonResponse(msg)


def qbuy_status(req, id):
    login_user = req.session.get('login_user')
    if not login_user:
        msg = {'code': 100, 'msg': '用户未登录'}
    else:
        # 判断是否已抢完
        user_id = login_user.get('user_id')
        if rd.hexists('qbuy', user_id):
            qbuy_goods_id = int(rd.hget('qbuy', user_id).decode())
            if qbuy_goods_id == id:
                msg = {'code': 200, 'msg': '抢购成功'}
            else:
                msg = {'code': 201, 'msg': '每位用户每天只能抢一次'}
        else:
            if rd.hlen('qbuy') >= 5:
                msg = {'code': 202,
                       'msg': '今日已抢完'}
            else:
                msg = {'code': 203,
                       'msg': '正在抢'}
                qbuy_task.delay(user_id, id)

    return JsonResponse(msg)
