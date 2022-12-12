from django.urls import path
from . import views
urlpatterns = [
    # items
    path("items/", views.item_index, name="items.index"),
    path("items/edit/", views.item_edit, name="items.edit"),
    path("items/create/", views.item_create, name="items.create"),
    path("items/show/", views.item_show, name="items.show"),

    #  users
    path("users/login/", views.user_login, name="users.login"),
    path("users/register/", views.user_register, name="users.register"),
]