import xadmin as admin

# Register your models here.
from goodsapp.models import Category, Goods, GoodsDetail, Cover, Storage


@admin.sites.register(Category)
class CategoryAdmin(object):
    list_display = ('title', 'level', 'parent')


@admin.sites.register(Goods)
class GoodsAdmin(object):
    list_display = ('name', 'price', 'category')


@admin.sites.register(GoodsDetail)
class GoodsDetailAdmin(object):
    list_display = ('goods', 'info')


@admin.sites.register(Cover)
class CoverAdmin(object):
    list_display = ('title', 'cover', 'width', 'height')


@admin.sites.register(Storage)
class StorageAdmin(object):
    list_display = ('goods', 'total_count')