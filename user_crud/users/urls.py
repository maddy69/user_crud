from django.urls import path
from .views import user_list, user_detail, user_create, user_edit, user_delete

app_name = 'users'

urlpatterns = [
    path('', user_list, name='user_list'),
    path('users/', user_list, name='user_list'),
    path('user/<int:pk>/', user_detail, name='user_detail'),
    path('user/new/', user_create, name='user_create'),
    path('user/<int:pk>/edit/', user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', user_delete, name='user_delete'),
]
