from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from custom_user.models import MyCustomUser

class MyCustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyCustomUser

class MyCustomUserAdmin(UserAdmin):
    form = MyCustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': (
                'homepage',
                'display_name',
                'age',
                'favorite_color'
            )}),
    ) 

admin.site.register(MyCustomUser, MyCustomUserAdmin)