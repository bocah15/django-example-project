from django import forms
from .models import Inventaris

class FormInventaris(forms.ModelForm):
	class Meta:
		model = Inventaris
		exclude = ('id',)

	def __init__(self, *args, **kwargs):
	  super(FormInventaris, self).__init__(*args, **kwargs)
	  for visible in self.visible_fields():
	    visible.field.widget.attrs['class'] = 'form-control form-control-sm'