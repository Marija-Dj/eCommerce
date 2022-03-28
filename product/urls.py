from pydoc import visiblename
from django.urls import path

from . import views

app_name= 'product'

urlpatterns = [
    path('', views.all_products, name='all_products' ),
    path('i/<slug:slug>/', views.detail_product, name="detail_product"),
    path('shoop/<slug:category_slug>/', views.category_list, name='category_list'),
]
