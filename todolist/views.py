# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import TodoForm, CreateUserForm


def registerPage(request): 
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Аккаунт с логином ' + user + ' успешно зарегестрирован')
                return redirect('loginPage')

        context = {'form':form}
        return render(request, 'loginForm/regPage.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info('Username OR password invalid')

        context = {}
        return render(request,'loginForm/loginPage.html')

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url = 'loginPage')
def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form':form}
    return render(request, 'todolist/index.html',context)


@require_POST
def addTodo(request): 
    form = TodoForm(request.POST)
    print(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'], username=request.POST['username'])
        new_todo.save()

    return redirect('index')

@login_required(login_url = 'loginPage')
def completeTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    
    return redirect('index')

@login_required(login_url = 'loginPage')
def deleteCompleted(request):
    Todo.objects.filter(complete__exact = True).delete()

    return redirect('index')

@login_required(login_url = 'loginPage')
def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')