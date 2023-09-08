from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signupPage.html"
    success_url = reverse_lazy("login")