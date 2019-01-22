from django.shortcuts import render

# Create your views here.
def regist(request):
    return render(request, 'user/regist.html', locals())