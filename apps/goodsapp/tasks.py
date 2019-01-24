import time

from XGS.celery import app


@app.task
def qbuy_task(user_id, goods_id):
    # 异步任务被执行时的code
    time.sleep(5)
    print(f'用户{user_id}正抢 {goods_id} 商品')
    return f'{user_id} 用户抢购成功'
