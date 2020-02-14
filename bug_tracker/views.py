from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from custom_user.models import MyCustomUser

from bug_tracker.models import Ticket
from bug_tracker.forms import CreationForm, LoginForm, AddTicketForm

@login_required()
def index(request):
    new_tickets = Ticket.objects.filter(ticket_status=Ticket.NEW)
    in_prog_tickets = Ticket.objects.filter(ticket_status=Ticket.INPROG)
    done_tickets = Ticket.objects.filter(ticket_status=Ticket.DONE)
    invalid_tickets = Ticket.objects.filter(ticket_status=Ticket.INVALID)

    return render(request, 'index.html', {
        'new_tickets': new_tickets,
        'in_prog_tickets': in_prog_tickets,
        'done_tickets': done_tickets,
        'invalid_tickets': invalid_tickets

    })


@login_required()
def add_ticket_view(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        
        if form.is_valid():
            ticket = form.save(commit=False)
            current_user = MyCustomUser.objects.get(id=request.user.id)
            ticket.submitted_by = current_user
            ticket.save()
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'generic_form.html', {
        'form': AddTicketForm()
    })


@login_required()
def creation_view(request):
    return render(request, 'generic_form.html', {
        'form': CreationForm()
    })


def login_view(request):
    return render(request, 'generic_form.html', {
        'form': LoginForm()
    })