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

class EditTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'ticket_status',
            'assigned_to'
        ]

    def __init__(self, *args, **kwargs):
        super(EditTicketForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].required=False

    def clean(self):
        cleaned_data = super().clean()
        ticket_status = cleaned_data.get('ticket_status')

        if ticket_status == 'DONE':
            cleaned_data['assigned_to'] = None
        elif ticket_status == 'INPROG':
            if not cleaned_data['assigned_to']:
                self.add_error(
                    'assigned_to',
                    'You need to assign someone to this ticket'
                )
            cleaned_data['completed_by'] = None
        elif ticket_status == 'INVALID':
            cleaned_data['assigned_to'] = None
            cleaned_data['completed_by'] = None
        
        return cleaned_data