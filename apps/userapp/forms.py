from django import forms
from django.core.exceptions import ValidationError

from userapp.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=20,
                               min_length=8,
                               error_messages={
                                   'required': '口令不能为空',
                                   'min_length': '口令不能少于 8 位字符',
                                   'max_length': '口令不能超出 20 位字符'
                               }, label='口令')

    password2 = forms.CharField(label='重复口令',
                                min_length=8)

    class Meta:
        model = UserProfile
        fields = '__all__'
        error_messages = {
            'username': {
                'required': '用户名不能为空',
                'unique': '用户名已存在！'
            }
        }

    def clean_password2(self):
        # 自定义验证
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')

        if p1 == p2:
            return p2
        else:
            # 收集错误
            raise ValidationError('两次口令不相同')
