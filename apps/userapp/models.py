from django.contrib.auth.hashers import make_password
from django.db import models

import base


# Create your models here.
class UserProfile(base.BaseModel):
    username = models.CharField(max_length=20,
                                verbose_name='用户名',
                                unique=True)

    password = models.CharField(max_length=100,
                                verbose_name='口令')

    email = models.CharField(max_length=50,
                             verbose_name='邮箱',
                             blank=True,
                             null=True)

    phone = models.CharField(max_length=11,
                             verbose_name='手机',
                             blank=True,
                             null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.password.startswith('pbkdf2_sha256') and len(self.password) < 30:
            self.password = make_password(self.password)  #  check_password('明文', '密文')

        super().save()

    def __str__(self):
        return self.username


    class Meta:
        db_table = 'app_user'
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name
        ordering = ['-last_time']