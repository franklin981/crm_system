from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Agent, Lead
# Create your views here.


def homepage(request):
    leads = Lead.objects.all()
    context = {
        leads: "leads"
    }
    return render(request, 'leads/home.html', context)

def feedback(request):
    return render(request, 'next.html')