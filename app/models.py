from django.db import models

# Create your models here.
from django.db import models
from shortuuidfield import ShortUUIDField


class User(models.Model):
    uid = ShortUUIDField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    favorite = models.CharField(max_length=200, default='[]')

    def __str__(self):
        return self.username


class apartment(models.Model):
    name = models.CharField(max_length=50, null=False, db_index=True)
    img = models.CharField(max_length=2000)
    price = models.CharField(max_length=50, null=False)
    information = models.CharField(max_length=500)
    facilities = models.CharField(max_length=500)
    rent_includes = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    address_link = models.CharField(max_length=500)
    score = models.IntegerField()
    comments = models.TextField(max_length=2000)
    is_delete = models.BooleanField(default=False)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'apartment'

    def __str__(self):
        return self.name


class evaluation(models.Model):
    apartment_id = models.IntegerField()
    user_id = ShortUUIDField()
    environment = models.IntegerField()
    staff_service = models.IntegerField()
    security = models.IntegerField()
    cost_performance = models.IntegerField()
    comment = models.CharField(max_length=2000)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'evaluation'