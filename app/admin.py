from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.apartment)
class Apartment(admin.ModelAdmin):
    list_display = ('name', 'price', 'score', 'is_delete', 'create_time', 'update_time')


@admin.register(models.evaluation)
class Evaluation(admin.ModelAdmin):
    list_display = ('environment', 'staff_service', 'security', 'cost_performance', 'comment', 'create_time'
                    , 'update_time')
