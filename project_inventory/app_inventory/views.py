from django.shortcuts import render

# Create your views here.
def item_index(request):
    return render(request, "items/index.html")

def item_show(request):
    return render(request, "items/show.html")

def item_edit(request):
    return render(request, "items/edit.html")

def item_create(request):
    return render(request, "items/create.html")

def user_login(request):
    return render(request, "users/login.html")

def user_register(request):
    return render(request, "users/register.html")