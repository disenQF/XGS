import xadmin as admin

from orderapp.models import OrderRecord


# Register your models here.


@admin.sites.register(OrderRecord)
class OrderRecordAdmin(object):
    def avg_count(self, obj):
        return int(obj.order_cancel / obj.order_count)

    avg_count.short_description = "Sum Count"
    avg_count.allow_tags = True
    avg_count.is_column = True

    list_display = ("date", "order_count", "order_cancel_count", 'order_price', 'order_cancel_price')
    list_display_links = ("date",)

    list_filter = ["date", "order_count", "order_cancel_count"]
    actions = None
    aggregate_fields = {"order_count": "sum", 'order_price': 'sum', "order_cancel_count": "sum",
                        'order_cancel_price': 'sum'}

    refresh_times = (3, 5, 10)
    data_charts = {
        "order": {'title': u"订单统计",
                  "x-field": "date",
                  "y-field": ("order_count", "order_price"),
                  "order": ('date',)},
        "order_cancel": {'title': u"取消订单统计",
                         "x-field": "date",
                         "y-field": ('order_cancel_count', 'order_cancel_price'), "order": ('date',)},
        "per_month": {'title': u"月度统计",
                      "x-field": "_chart_month",
                      "y-field": ("order_count",),
                      "option": {
                          "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
                          "xaxis": {"aggregate": "sum", "mode": "categories"},
                      },
                      },
    }

    def _chart_month(self,  obj):
        print('--------->',obj.date)
        return obj.date.strftime("%m")
