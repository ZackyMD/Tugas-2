from django.urls import path
from todolist.views import show_todolist
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import get_task #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import cek
from todolist.views import hapus

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', get_task, name='get_task'), #sesuaikan dengan nama fungsi yang dibuat
    path('cek/<int:pk>/', cek, name='cek'),
    path('hapus/<int:pk>/', hapus, name='hapus'),
]