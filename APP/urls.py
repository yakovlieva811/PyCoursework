from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_sho, name='insert-sho'),
    path('show/', views.show_sho, name='show-sho'),
    path('edit/<int:pk>', views.edit_sho, name='edit-sho'),
    path('remove/<int:pk>', views.remove_sho, name='remove-sho'),
]