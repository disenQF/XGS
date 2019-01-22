import xadmin as admin
from xadmin import views

from userapp.models import UserProfile


@admin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@admin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    global_search_models = [UserProfile]
    global_models_icon = {
        UserProfile: "fa fa-laptop"
    }
    apps_label_title = {
        'userapp': '客户管理'
    }
    menu_style = 'accordion'  # 'accordion', 'default'


@admin.sites.register(UserProfile)
class UserProfileAdmin(object):
    list_display = ('username', 'email', 'phone', 'last_time')
    list_display_links = ('username', )
    list_filter = ['username']

    search_fields = ['username', 'phone']
