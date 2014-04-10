from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)

    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)


class LoginRequiredMx(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super (LoginRequiredMx, self).dispatch(*args, **kwargs)
##HOW-TO make yours view Login Protected - just inherit form that class in your view ##


