from django.urls import path
from goodsapp import views

urlpatterns = [
    path('show/<int:id>/', views.show),
    path('qbuy/<int:id>/', views.qbuy),
    path('qbuy_status/<int:id>/', views.qbuy_status),
]
