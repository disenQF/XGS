import os
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from XGS import settings
from userapp.models import UserProfile


def regist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        photo = request.POST.get('photo')

        # 按照文件路径分隔出文件名
        file_name = os.path.split(photo)[-1]

        # 将临时的文件，变成持久文件
        full_photo = os.path.join(settings.BASE_DIR, 'static/'+photo)
        to_full_photo = os.path.join(settings.BASE_DIR, f'static/images/{file_name}')
        os.rename(full_photo, to_full_photo)

        UserProfile.objects.create(username=username,
                                   password=password,
                                   photo=f'images/{file_name}')

        # 删除tmp临时文件目录
        tmp_dir = os.path.join(settings.BASE_DIR, 'static/images/tmp')
        os.system(f'rm -rf {tmp_dir}')

        return redirect('/admin/')

    return render(request, 'user/regist.html', locals())


@csrf_exempt
def upload(request):

    # 获取上传文件
    photoFile: InMemoryUploadedFile = request.FILES.get('photo')  # key是前端上传文件的FieldName

    # 将上传的文件保存到 /static/images/tmp目录中
    dir_ = os.path.join(settings.BASE_DIR, 'static/images/tmp')

    # 生成新的文件名
    file_name = uuid.uuid4().hex+ ('.jpg' if photoFile.content_type.endswith('jpeg') else '.png')

    # 按文件的段方式写入到新的文件中(服务器的文件)
    with open(os.path.join(dir_, file_name), 'wb') as f:
        for chunk in photoFile.chunks():
            f.write(chunk)

    # 响应json数据
    return JsonResponse({'msg': 1,
                         'path': f'images/tmp/{file_name}'})
