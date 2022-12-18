from django.shortcuts import render, redirect
from .forms import ItemCreateForm, UserLoginForm, UserRegisterForm
from datetime import datetime
from .models import Item, AppUser

# Create your views here.
def item_index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, "items/index.html", context)

def item_show(request, id):
    data = Item.objects.get(id=id)
    context = {"data": data}
    return render(request, "items/show.html", context)

def item_edit(request, id):
    data = Item.objects.get(id=id)
    context = {"data": data}
    return render(request, "items/edit.html", context)

def item_update(request):
    if request.method == "POST":
        item_obj = Item.objects.get(id=request.POST.get("id"))
        user = AppUser.objects.get(id=1)
        item_obj.title = request.POST.get("title")
        item_obj.particular = request.POST.get("particular")
        item_obj.lf = request.POST.get("lf")
        item_obj.price = request.POST.get("price")
        item_obj.quantity = request.POST.get("quantity")
        item_obj.total = request.POST.get("total")
        item_obj.added_at = datetime.now()
        item_obj.user = user
        item_obj.save()

    return redirect("items.index")

def item_delete(request, id):
    data = Item.objects.get(id=id)
    data.delete()
    return redirect("items.index")

def item_create(request):
    form = ItemCreateForm()
    context = {"form": form}
    if request.method == "POST":
        item_obj = Item()
        user = AppUser.objects.get(id=1)
        item_obj.title = request.POST.get("title")
        item_obj.particular = request.POST.get("particular")
        item_obj.lf = request.POST.get("lf")
        item_obj.price = request.POST.get("price")
        item_obj.quantity = request.POST.get("quantity")
        item_obj.total = request.POST.get("total")
        item_obj.added_at = datetime.now()
        item_obj.user = user
        item_obj.save()
        context.setdefault("msg", "Item Created Successfully")
    return render(request, "items/create.html", context)

def user_login(request):
    form = UserLoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)

def user_register(request):
    form = UserRegisterForm()
    context = {"form": form}
    if request.method == "POST":
        user = AppUser()
        user.full_name = request.POST["full_name"]
        user.email = request.POST["email"]
        user.contact = request.POST["contact"]
        user.password = request.POST["password"]
        user.save()
        context.setdefault("msg", "Registered Successfully")
    return render(request, "users/register.html", context)