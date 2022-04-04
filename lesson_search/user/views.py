from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserForm


class RegisterView(CreateView):
    form_class = UserForm
    template_name = 'pages-register.html'
    success_url = reverse_lazy('client_list')



