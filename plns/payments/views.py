from django.views.generic.edit import CreateView
from django import forms
from django.template import RequestContext
from django.views.generic.edit import FormView

from plns.payments.forms import CategoryAddForm
from plns.payments.models import Category


class Categories(FormView):
	form_class = CategoryAddForm
	template_name = "payments/categorys.html"

	def get_form_kwargs(self):
	    kwargs = super(Categories, self).get_form_kwargs()
	    kwargs['user'] = self.request.user
	    return kwargs

	def get_context_data(self, **kwargs):
	    kwargs = super(Categories, self).get_context_data(**kwargs)
	    kwargs['nodes'] = Category.objects.filter(user_id=self.request.user.id)
	    return kwargs

	def form_valid(self, form):
	    category = form.save(commit=False)
	    category.user_id = self.request.user.id
	    category.save()
	    
