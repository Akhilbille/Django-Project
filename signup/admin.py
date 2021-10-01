from . import models
from django.contrib import admin

from django.contrib.auth.models import User
# Register your models here.



@admin.register(models.Proffesional_detail)
class Proffesional_detailAdmin(admin.ModelAdmin):
    list_display = ['user','departments','occupation','occupation_Location','office_Levels','office_Location','organisation','districts','constituency','mandal','panchayath','village','central_Organisation']
    list_filter = ['departments','occupation','occupation_Location','office_Levels','office_Location','organisation','districts','constituency','mandal','panchayath','village','central_Organisation']
    search_fields = ['user__username','departments__istartswith','occupation__istartswith','occupation_Location__istartswith','office_Levels__istartswith','office_Location__istartswith','organisation__istartswith','districts__istartswith','constituency__istartswith','mandal__istartswith','panchayath__istartswith','village__istartswith','central_Organisation__istartswith']




class WebUser(User):

    class Meta:
        proxy = True
        verbose_name = "User"
        verbose_name_plural = "Users"


class UserAdmin(admin.ModelAdmin):

    list_display = ['username','first_name','last_name','email','date_joined']
    list_filter = ['date_joined']
    # search_fields = ('user__username', 'user__email')

admin.site.register(WebUser, UserAdmin)