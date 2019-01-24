from django.urls import path
from userapp import views

urlpatterns = [
    path('regist/', views.regist),
    path('login/', views.login),
    path('upload/', views.upload),
]
