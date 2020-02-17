"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bug_tracker import views
from bug_tracker.models import Ticket

try:
    admin.site.register(Ticket)
except Exception:
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('login/', views.login_view),
    path('createuser/', views.creation_view),
    path('addticket/', views.add_ticket_view),
    path('edit/<int:ticket_id>', views.edit_ticket_view),
    path('ticket/<int:ticket_id>', views.ticket_detail_view),
    path('user/<int:user_id>', views.user_detail_view),
]
