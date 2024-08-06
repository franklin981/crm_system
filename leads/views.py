from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Agent, Lead
# Create your views here.


def lead_list(request):
    leads = Lead.objects.all()
    agents = Agent.objects.all()
    context = {
        "leads": leads,
        "agents": agents,
    }
    return render(request, 'leads/lead_home.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, 'leads/lead_details.html', context)