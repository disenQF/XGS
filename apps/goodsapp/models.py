from django.db import models

# Create your models here.
import base


class Category(base.BaseModel):
    levels = ((0, '一级分类'),
              (1, '二级分类'),
              (2, '三级分类'))

    title = models.CharField(max_length=20,
                             verbose_name='分类名')
    cover = models.ImageField(verbose_name='分类封面',
                              upload_to='category',
                              blank=True,
                              null=True)
    level = models.IntegerField(verbose_name='分类等级',
                                choices=levels)

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               verbose_name='父级分类',
                               blank=True,
                               null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_category'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


class Goods(base.BaseModel):
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='所属分类')

    name = models.CharField(max_length=50,
                            verbose_name='商品名称')
    price = models.DecimalField(verbose_name='商品单价',
                                max_digits=10,
                                decimal_places=2)
    barcode = models.CharField(verbose_name='条形码',
                               max_length=50)

    cover = models.ImageField(verbose_name='封面',
                              upload_to='goods')

    class Meta:
        db_table = 'app_goods'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name


# 后期存放到云存储中
class Cover(base.BaseModel):
    title = models.CharField(max_length=50,
                             verbose_name='标题')

    cover = models.ImageField(verbose_name='图片',
                              upload_to='images',
                              width_field='width',
                              height_field='height')

    width = models.IntegerField(verbose_name='宽度')
    height = models.IntegerField(verbose_name='高度')

    class Meta:
        db_table = 'app_cover'
        verbose_name = '图片管理'
        verbose_name_plural = verbose_name


class GoodsDetail(base.BaseModel):
    goods = models.ForeignKey(Goods,
                              on_delete=models.CASCADE)

    covers = models.ManyToManyField(Cover)
    info = models.TextField(verbose_name='详情描述')

    class Meta:
        db_table = 'app_goodsdetail'
        verbose_name = '商品详情'
        verbose_name_plural = verbose_name


class Storage(base.BaseModel):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,
                              verbose_name='商品名称')
    total_count = models.IntegerField(verbose_name='存量',
                                      default=100)

    class Meta:
        db_table = 'app_storage'
        verbose_name = '库存信息'
        verbose_name_plural = verbose_name
