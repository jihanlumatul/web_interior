from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('all/', views.product_list, name='products'),
    path('<int:id>/', views.product_detail, name='product_detail'),
]
