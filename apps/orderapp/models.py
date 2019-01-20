from django.db import models

# Create your models here.
class OrderRecord(models.Model):
    date = models.DateField(auto_now_add=True,
                            verbose_name='日期')
    order_count = models.IntegerField(verbose_name='订单数量')
    order_price = models.FloatField(verbose_name='订单总金额')
    order_cancel_count = models.IntegerField(verbose_name='取消订单数量')
    order_cancel_price = models.FloatField(verbose_name='取消订单金额')

    def __str__(self):
        return "%s Order Record" % self.date.strftime('%Y-%m-%d')

    class Meta:
        db_table = 'order_record'
        verbose_name = '订单统计'
        verbose_name_plural = verbose_name