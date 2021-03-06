from django.urls import reverse_lazy
from django.views import generic

from applications.custom_auth.forms import CustomUserCreationForm


class CustomRegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

