from django.db import models
import base

# Create your models here.
from userapp.models import UserProfile


class OrderRecord(models.Model):
    date = models.DateField(verbose_name='日期')
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

class Address(base.BaseModel):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE,
                             verbose_name='所属用户')
    phone = models.CharField(verbose_name='手机号', max_length=11)
    info = models.CharField(max_length=100,
                            verbose_name='收货地址')
    is_default = models.BooleanField(verbose_name='默认地址',
                                     default=False)

    class Meta:
        db_table = 'app_address'
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name


class Order(base.BaseModel):

    pay_types = ((0, '余额'), (1, '支付宝'), (2, '微信'))
    pay_all_status = ((0, '待支付'),
                      (1, '已支付'),
                      (2, '已评价'),
                      (3, '已退款'))

    title = models.CharField(max_length=200,
                             verbose_name='标题')
    price = models.DecimalField(verbose_name='订单金额',
                                max_digits=10,
                                decimal_places=2)
    pay_type = models.IntegerField(verbose_name='支付类型',
                                   choices=pay_types,
                                   default=0)

    pay_statue = models.IntegerField(verbose_name='订单状态',
                                     choices=pay_all_status,
                                     default=0)

    address = models.ForeignKey(Address,
                                verbose_name='收货信息',
                                on_delete=models.SET_NULL,
                                null=True)

    # 实现自增的订单号:  201901230000001
    order_num = base.OrderNumAutoField(max_length=15,
                                       verbose_name='订单号')

    class Meta:
        db_table = 'app_order'
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name