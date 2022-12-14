from django.shortcuts import render
from .forms import ItemCreateForm, UserLoginForm, UserRegisterForm
from datetime import datetime
from .models import Item, AppUser

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
    if request.method == "POST":
        item = Item()
        user = AppUser.objects.get(id=1)
        item.title = request.POST.get("title")
        item.particular = request.POST.get("particular")
        item.lf = request.POST.get("lf")
        item.price = request.POST.get("price")
        item.quantity = request.POST.get("quantity")
        item.total = request.POST.get("total")
        item.added_at = datetime.now()
        item.user = user
        item.save()
        context.setdefault("msg", "Item Created Successfully")
        # item = Item(title=title, particular=particular)
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