from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from cats.models import Breed, Cat


class CatList(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.count()
        cl = Cat.objects.all()

        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, 'cats/cat_list.html', ctx)
    
class BreedView(LoginRequiredMixin, View): 
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)
    
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

    

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_form.html'

    

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_confirm_delete.html'


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')



