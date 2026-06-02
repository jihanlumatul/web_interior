from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('all/', views.product_list, name='products'),
    path('custom/', views.custom_page, name='custom'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
]
