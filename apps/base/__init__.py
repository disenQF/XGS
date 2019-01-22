from django.db import models


class BaseModel(models.Model):
    add_time = models.DateTimeField(verbose_name='新增时间',
                                    auto_now_add=True)

    last_time = models.DateTimeField(verbose_name='修改时间',
                                     auto_now=True)

    class Meta:
        abstract = True
