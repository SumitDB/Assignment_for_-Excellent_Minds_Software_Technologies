from django.contrib import admin
from .models import User, Skill, City

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','skill','city')

@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display=('id','skills')

@admin.register(City)
class City(admin.ModelAdmin):
    list_display=('id','city')