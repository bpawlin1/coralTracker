from django.shortcuts import render
from coral.models import Coral
from django.views.generic import ( CreateView, UpdateView,DeleteView,DetailView, ) # new
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy  # new
from .forms import CoralForm  # new
from django.views.generic import CreateView


# Create your views here.
 
def index(request):
    coral = Coral.objects.all()
    context = {'corals': coral}
    return render(request, 'index.html', context)

def coral_detail(request, pk):
    coral = Coral.objects.get(pk=pk)
    context = {
        'coral': coral
    }
    return render(request, 'coral_detail.html', context)

class CreateCoralView(SuccessMessageMixin,CreateView):  # new
    model = Coral
    form_class = CoralForm
    template_name = "newCoral.html"
    success_message = "Your coral was added!"
    success_url = reverse_lazy("index")
    



class UpdateCoralView(SuccessMessageMixin, UpdateView):
    model = Coral
    template_name = "updateCoral.html"
    form_class = CoralForm

    success_message = "Your entry was updated!"
    success_url = reverse_lazy("index")
    

class DeleteCoralView(DeleteView):
    model = Coral
    form_class = CoralForm
    template_name = "coralDelete.html"
    success_message = "Your entry was deleted!"
    success_url = reverse_lazy("index")
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)