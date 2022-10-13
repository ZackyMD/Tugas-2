from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from todolist.models import Task

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    toDolist = Task.objects.filter(user=request.user)
    if request.method == 'POST':
        temp = ToDoList(user=request.user, title=request.POST.get('title'), description=request.POST.get('description'))
        temp.save()
        return JsonResponse({'message': 'success'})

    context = {
    'nama' : request.user.username,
    'todolist' : toDolist,
    'last_login': request.COOKIES['last_login'],

    }
    return render(request, "todolist.html", context)

# tampilan baru untuk /json 
@login_required(login_url='/todolist/login/')
def show_json(request:HttpResponse):
    dataToDoList = Task.objects.filter(user=request.user)
    context = {
        'nama' : request.user.username,
        'todolist' : dataToDoList,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

# get data AJAX
def get_json(request):
    dataToDoList = Task.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize("json", dataToDoList), content_type="application/json")

# add Task di modal
def create_todolist(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date=datetime.now()
        user=request.uuser

        Task.objects.create(
            title=title,
            description=description,
            date=date,
            user=user,

        )

    return HttpResponse(b"CREATED", status=201)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def cek(request, pk):
    temp = Task.objects.get(id=pk)
    if (temp.finish == False):
        temp.finish = True
    else :
        temp.finish = False
    temp.save()
    return redirect('todolist:show_todolist')

def hapus(request, pk):
    item = Task.objects.filter(pk=pk)
    item.delete()
    return redirect('todolist:show_todolist')

def get_task(request):
    context = {}
    if request.method == 'POST' :
        wadah = Task(user=request.user, title=request.POST.get('title'), description=request.POST.get('description'))
        wadah.save()
        return redirect('todolist:show_todolist')
    return render(request, "create-task.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response