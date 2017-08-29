from django.contrib import admin
from .models import Base, Chronicle, Abilities, Attributes, Spheres, TechnocracySpheres


@admin.register(Chronicle)
class BaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    pass

@admin.register(Abilities)
class AbilitiesAdmin(admin.ModelAdmin):
    pass

@admin.register(Attributes)
class AttributesAdmin(admin.ModelAdmin):
    pass

@admin.register(Spheres)
class SpheresAdmin(admin.ModelAdmin):
    pass

@admin.register(TechnocracySpheres)
class TechnocracySpheresAdmin(admin.ModelAdmin):
    pass