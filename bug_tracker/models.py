from django.db import models
from django.utils import timezone

from custom_user.models import MyCustomUser

class Ticket(models.Model):
    NEW = 'NEW'
    INPROG = 'INPROG'
    DONE = 'DONE'
    INVALID = 'INVALID'

    status_choices = [
        (NEW, 'New'),
        (INPROG, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]

    title = models.CharField(max_length=200)

    date_submitted = models.DateTimeField(default=timezone.now)

    description = models.CharField(max_length=400)

    ticket_status = models.CharField(
        max_length=11,
        choices=status_choices,
        default=NEW
    )

    submitted_by = models.ForeignKey(MyCustomUser,
        related_name='submitted_by',
        on_delete=models.SET_NULL,
        null=True
    )

    assigned_to = models.ForeignKey(MyCustomUser,
        related_name='assigned_to',
        default=None,
        on_delete=models.SET_NULL,
        null=True
    )
    
    completed_by = models.ForeignKey(MyCustomUser,
        related_name='completed_by',
        default=None,
        on_delete=models.SET_NULL,
        null=True
    )