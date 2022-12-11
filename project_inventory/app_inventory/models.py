from django.db import models

# Create your models here.
class AppUser(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "app_users"

class Item(models.Model):
    title = models.CharField(max_length=100)
    particular = models.CharField(max_length=200)
    lf = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(max_length=20)
    price = models.FloatField(max_length=200)
    total = models.FloatField(max_length=200)
    added_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "app_items"
