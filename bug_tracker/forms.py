from django import forms
from django.contrib.auth.forms import UserCreationForm

from custom_user.models import MyCustomUser
from bug_tracker.models import Ticket

class CreationForm(UserCreationForm):
    class Meta:
        model = MyCustomUser
        fields = [
            'email',
            'username',
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
        ]