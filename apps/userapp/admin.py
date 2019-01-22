from crispy_forms.bootstrap import AppendedText
from crispy_forms.layout import Row

import xadmin as admin
from xadmin import views

from userapp.models import UserProfile
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Side, HTML, Col, Column
from xadmin.plugins.inline import Inline


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
    def img_path(self, obj):
        return "/static/"+obj.photo

    list_display = ('username', 'email', 'phone', 'last_time')
    list_display_links = ('username', )
    list_filter = ['username']

    search_fields = ['username', 'phone']

    form_layout = (
        Main(
            Fieldset("用户与口令", "username", 'password', description="required"),
            Fieldset('显示图片', 'photo', HTML('<img width=100 height=120 style="margin:10px;" src="/static/{{ form.photo.value }}">')),
            Fieldset(
                "邮箱与电话",
                'phone',
                'email'
            )
        ),
    )

    reversion_enable = True
