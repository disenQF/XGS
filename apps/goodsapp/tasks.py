import time

from XGS.celery import app
from base import rd


@app.task
def qbuy_task(user_id, goods_id):
    # 异步任务被执行时的code
    print(f'用户{user_id}正抢 {goods_id} 商品')
    if not rd.hexists('qbuy', user_id) and rd.hlen('qbuy') < 5:
        rd.hset('qbuy', user_id, goods_id)
        return f'{user_id} 用户抢购 {goods_id}成功'

    return f'{user_id} 用户抢购 {goods_id} 失败'
