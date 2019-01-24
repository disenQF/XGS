from django.db import models


# Create your models here.
class Active(models.Model):

    active_types = ((0, '全场折扣'),
                    (1, '限时折扣'))

    title = models.CharField(max_length=100,
                             verbose_name='活动标题')

    cover = models.ImageField(verbose_name='活动图片',
                              upload_to='actives')

    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')

    active_type = models.IntegerField(verbose_name='活动类型',
                                      choices=active_types)

    discount = models.DecimalField(verbose_name='折扣率',
                                   default=0.88,
                                   max_digits=4,
                                   decimal_places=2)

    def __str__(self):
        return self.title

    @property
    def active_type_name(self):
        return self.active_types[self.active_type][1]

    class Meta:
        db_table = 'app_active'
        verbose_name = '活动管理'
        verbose_name_plural = verbose_name