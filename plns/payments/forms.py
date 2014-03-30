from django import forms
from plns.payments.models import Category

class CategoryAddForm(forms.ModelForm):
	
	class Meta:
		model=Category
		fields = {"name", "parent"}
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(CategoryAddForm, self).__init__(*args, **kwargs)
		self.fields['parent'] = forms.ModelChoiceField(queryset=Category.objects.filter(user_id=user.id), required=False)



