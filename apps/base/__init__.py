from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    add_time = models.DateTimeField(verbose_name='新增时间',
                                    auto_now_add=True)

    last_time = models.DateTimeField(verbose_name='修改时间',
                                     auto_now=True)

    class Meta:
        abstract = True


class OrderNumAutoField(models.CharField):
    def get_db_prep_value(self, value, connection, prepared=False):
        if value is not None:
            if len(value) == 15:
                # 验证当前数据库的真实的数据??
                return value
            else:
                raise ValueError('此字段不能修改')

        current_date = datetime.today().strftime('%Y%m%d')  # 当前的日期

        # 1. 从订单表中查找最大的订单号
        cursor = connection.cursor()
        cursor.execute('select max(order_num) from app_order')
        last_order_num = cursor.fetchone()[0]
        print('---OrderNumAutoField-----', last_order_num)
        # 2. 拆分格式:  日期+序号
        num = 1
        if last_order_num:
            last_date = last_order_num[:8]
            # 3. 比较日期，如果与当前日期是同一天，序号加1，生成新的订单号
            #              如果不是当天，则创建新的订单号，序号为1
            if last_date == current_date:
                num = int(last_order_num[8:])+1

        # 4. 返回新的订单号
        num_str = str(num).rjust(7, '0')
        return f'{current_date}{num_str}'
