from django.urls import path
from goodsapp import views

urlpatterns = [
    path('show/<int:id>/', views.show),
]
