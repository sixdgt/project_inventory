from django.urls import path
from . import views
urlpatterns = [
    path("items/", views.item_index, name="items.index"),
    path("items/edit/", views.item_edit, name="items.edit"),
    path("items/create/", views.item_create, name="items.create"),
    path("items/show/", views.item_show, name="items.show"),
]