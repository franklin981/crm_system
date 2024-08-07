from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Agent, Lead
from .forms import LeadForm, LeadModelForm
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


# CREATE A LEAD

# def lead_create(request):
#     print(request.POST)
#     form = LeadForm() # why this comes first is print the form when request has not been submitted
#     if request.method == "POST":
#         form = LeadForm(request.POST) # if the submit is clicked, the collect the post data in the form and send to the context dict
#         if form.is_valid():
#             print("form is valid")
#             print(form.cleaned_data) # cleaned_Data shows u the a well formatted data from the form
#             #lets get all the clean data 
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first() # pics the first agent in the data base
            
#             lead = Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print("Lead has been create")
#             return redirect('/leads/lead_list')
#     context = {
#         "form": form
#     }
#     return render(request, 'leads/lead_create.html', context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']
            
            # create the lead to the database
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            
            # redirect back to the lead list
            return redirect('/leads/lead_list')
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)