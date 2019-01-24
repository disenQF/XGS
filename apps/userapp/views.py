import json
import os
import uuid

from django.contrib.auth.hashers import check_password
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from XGS import settings
from userapp.models import UserProfile
from userapp.forms import UserForm

def regist(request):

    if request.method == 'POST':
        form = UserForm(request.POST)  # 自动将POST中的数据提取出来

        # 验证是否存在错误
        if form.is_valid():
            # 按照文件路径分隔出文件名

            # cleaned_data 是去除所有字段两边空白后的数据字典
            photo = form.cleaned_data.get('photo')
            print(photo)
            if photo:
                file_name = os.path.split(photo)[-1]

                # 将临时的文件，变成持久文件
                full_photo = os.path.join(settings.BASE_DIR, 'static/'+photo)
                to_full_photo = os.path.join(settings.BASE_DIR, f'static/images/{file_name}')
                os.rename(full_photo, to_full_photo)

                form.photo = f'images/{file_name}'

                # 删除tmp临时文件目录
                tmp_dir = os.path.join(settings.BASE_DIR, 'static/images/tmp')
                os.system(f'rm -rf {tmp_dir}')

            form.save()  # 保存数据

            return redirect('/admin/')
        else:
            # 将errors的html字符串转成json字符串
            errors = json.loads(form.errors.as_json())
            print(errors)

    return render(request, 'user/regist.html', locals())


@csrf_exempt
def upload(request):

    # 获取上传文件
    photoFile: InMemoryUploadedFile = request.FILES.get('photo')  # key是前端上传文件的FieldName

    # 将上传的文件保存到 /static/images/tmp目录中
    dir_ = os.path.join(settings.BASE_DIR, 'static/images/tmp')
    if not os.path.exists(dir_):
        os.mkdir(dir_)

    # 生成新的文件名
    file_name = uuid.uuid4().hex+ ('.jpg' if photoFile.content_type.endswith('jpeg') else '.png')

    # 按文件的段方式写入到新的文件中(服务器的文件)
    with open(os.path.join(dir_, file_name), 'wb') as f:
        for chunk in photoFile.chunks():
            f.write(chunk)

    # 响应json数据
    return JsonResponse({'msg': 1,
                         'path': f'images/tmp/{file_name}'})


def login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        result = UserProfile.objects.filter(username=username)
        if not result.exists():
            errors = {'username':f'{username} 不存在'}
        else:
            login_user = result.first()
            if check_password(password, login_user.password):
                req.session['login_user'] = {
                    'user_id': login_user.id,
                    'username': login_user.username,
                    'photo': login_user.photo
                }
            else:
                errors = {'password':'口令不正确'}

    return render(req, 'user/login.html', locals())