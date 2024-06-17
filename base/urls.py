from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage , name='homepage'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update/<int:item_id>/', views.update_item_form, name='update_item_form'),
    path('add/', views.add_item, name='add_item')
]
