from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', get_task, name='get_task'), #sesuaikan dengan nama fungsi yang dibuat
    path('cek/<int:pk>/', cek, name='cek'),
    path('hapus/<int:pk>/', hapus, name='hapus'),
    path('json/', get_json, name='get_json'),
    path('create_todolist/', create_todolist, name='create_todolist'),
    path('show_json/', show_json, name='show_json'),


]