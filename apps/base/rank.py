import base
from goodsapp.models import Goods


def add_week_rank(goods_id):
    redis = base.rd
    has_rank = redis.exists('week_rank')
    redis.zincrby('week_rank', 1, goods_id)
    if not has_rank:
        redis.expire('week_rank', 60*60*24*7)


def top_week_rank(n=5):
    ranks = base.rd.zrevrange('week_rank', 0, n-1, withscores=True)
    return [(Goods.objects.get(pk=id.decode()), int(score))
            for id, score in ranks]

