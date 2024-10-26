from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.views.decorators.http import require_GET, require_http_methods

from .forms import RegistrationForm


@method_decorator(require_GET, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'


@method_decorator(decorator=[login_required, require_GET], name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'


@method_decorator(require_http_methods(['GET', 'POST']), name='dispatch')
class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
