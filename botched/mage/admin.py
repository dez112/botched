from django.contrib import admin
from .models import Base, Chronicle


@admin.register(Chronicle)
class BaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    pass