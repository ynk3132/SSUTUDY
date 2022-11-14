from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
from django.http import HttpResponseRedirect 


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
            login(request, user)
        else:
            print("인증 실패")
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect("user:login")


def signup_view(request):
    if request.method=="POST":
        profile_img = request.FILES["profile_img"]
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]
        content = request.POST["content"]

        user = User.objects.create_user(username, email, password, content)
        user.last_name = lastname
        user.first_name = firstname
        user.student_id = student_id
        user.profile_img = profile_img
        user.content = content
        user.save()
        return redirect("user:login")

    return render(request, "users/signup.html")

def todoappView(request):
    all_todo_items = User.objects.all()
    return render(request, 'users/todo.html',
    {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = User(content = x)
    new_item.save()
    return HttpResponseRedirect('/users/todo/')