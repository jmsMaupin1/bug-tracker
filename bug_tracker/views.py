from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required

from custom_user.models import MyCustomUser

from bug_tracker.models import Ticket
from bug_tracker.forms import CreationForm, LoginForm, AddTicketForm, EditTicketForm

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
def edit_ticket_view(request, ticket_id):
    ticket = None
    form = None

    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Exception:
        return HttpResponseRedirect(reverse('homepage'))

    if request.method == 'POST':
        form = EditTicketForm(request.POST, instance=ticket)

        if form.is_valid():
            ticket = form.save(commit=False)
            if ticket.ticket_status == 'DONE':
                user = MyCustomUser.objects.get(id=request.user.id)
                ticket.completed_by = user
            ticket.save()
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = EditTicketForm(instance=ticket)
    
    return render(request, 'generic_form.html', {
        'form': form
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
def ticket_detail_view(request, ticket_id):
    ticket = None
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Exception:
        return HttpResponseRedirect(reverse('homepage'))

    ticket_states = {
        "NEW": "New",
        "INPROG": "In Progress",
        "DONE": "Done",
        "INVALID": "Invalid"
    }

    return render(request, 'ticket_detail.html', {
        'ticket': ticket,
        "status": ticket_states[ticket.ticket_status]
    })


@login_required()
def user_detail_view(request, user_id):
    user = None
    submitted_tickets = None
    assigned_tickets = None
    closed_tickets = None

    try:
        user = MyCustomUser.objects.get(id=user_id)
        submitted_tickets = Ticket.objects.filter(submitted_by=user)
        assigned_tickets = Ticket.objects.filter(assigned_to=user)
        closed_tickets = Ticket.objects.filter(completed_by=user)
    except Exception as e:
        print(e)
    
    return render(request, 'user_detail.html', {
        'user': user,
        'submitted_tickets': submitted_tickets,
        'assigned_tickets': assigned_tickets,
        'closed_tickets': closed_tickets
    })

@login_required()
def creation_view(request):
    form = None
    if request.method == 'POST':
        form = CreationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = MyCustomUser.objects.create_user(
                data['username'], data['email'], data['password1']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = CreationForm()

    return render(request, 'generic_form.html', {
        'form': form
    })


def login_view(request):
    form = None
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse='homepage')
        else:
            form=LoginForm()

    return render(request, 'generic_form.html', {
        'form': form
    })