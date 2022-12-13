from django.shortcuts import render
from .forms import ItemCreateForm, UserLoginForm, UserRegisterForm

# Create your views here.
def item_index(request):
    return render(request, "items/index.html")

def item_show(request):
    return render(request, "items/show.html")

def item_edit(request):
    return render(request, "items/edit.html")

def item_create(request):
    form = ItemCreateForm()
    context = {"form": form}
    return render(request, "items/create.html", context)

def user_login(request):
    form = UserLoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)

def user_register(request):
    form = UserRegisterForm()
    context = {"form": form}
    return render(request, "users/register.html", context)