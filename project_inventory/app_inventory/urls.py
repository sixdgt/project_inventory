from django.urls import path
from . import views
from .views import (ItemApiView, ItemIdApiView)
urlpatterns = [
    # items
    path("items/", views.item_index, name="items.index"),
    path("items/edit/<int:id>/", views.item_edit, name="items.edit"),
    path("items/create/", views.item_create, name="items.create"),
    path("items/update/", views.item_update, name="items.update"),
    path("items/show/<int:id>/", views.item_show, name="items.show"),
    path("items/delete/<int:id>/", views.item_delete, name="items.delete"),

    # users
    path("users/login/", views.user_login, name="users.login"),
    path("users/logout/", views.user_logout, name="users.logout"),
    path("users/register/", views.user_register, name="users.register"),

    # api
    path("api/items/", ItemApiView.as_view()),
    path("api/items/<int:id>/", ItemIdApiView.as_view()),
]