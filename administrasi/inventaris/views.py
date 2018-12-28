from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, View, UpdateView
from .models import Inventaris
from .forms import FormInventaris
from django.urls import reverse_lazy

# Create your views here.

class InventarisListView(LoginRequiredMixin, ListView):
	queryset = Inventaris.objects.all()
	template_name = 'inventaris/inventaris_list.html'

class InventarisCreateView(LoginRequiredMixin, CreateView):
	form_class = FormInventaris
	template_name = 'inventaris/inventaris_new.html'
	success_url = reverse_lazy('inventaris:inventaris_list')

class InventarisDeleteView(LoginRequiredMixin, View):
	def get(self, r, id):
		instansi = get_object_or_404(Inventaris, id=id)
		instansi.delete()
		return redirect ('inventaris:inventaris_list')

# class InventarisUpdateView(LoginRequiredMixin, UpdateView):
# 	model = Inventaris
# 	form_class = FormInventaris
# 	template_name = 'inventaris/inventaris_edit.html'

# 	def form_valid(self, form):
# 		self.object = form.save(commit=False)
# 		self.object.save()
# 		return redirect('inventaris:inventaris_list')

# 	@method_decorator(login_required)
# 	def dispatch(self, request, *args, **kwargs):
# 		return super(InventarisUpdateView, self).dispatch(request, *args, **kwargs)

class InventarisUpdateView(LoginRequiredMixin, UpdateView):
   model = Inventaris
   form_class = FormInventaris
   template_name = 'inventaris/inventaris_edit.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.save()
      return redirect("inventaris:inventaris_list")

   @method_decorator(login_required)
   def dispatch(self, request, *args, **kwargs):
      return super(InventarisUpdateView, self).dispatch(request, *args, **kwargs)