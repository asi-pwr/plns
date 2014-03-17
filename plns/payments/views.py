from plns.payments import Category
from django.views.generic.edit import CreateView
from django import forms

def show_categorys(request):
return render_to_response("categorys.html",
			{'nodes':Category.objects.all()},
			context_instance=RequestContext(request))

