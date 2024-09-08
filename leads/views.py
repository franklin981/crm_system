from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Agent, Lead
from .forms import LeadForm, LeadModelForm
from django.views.generic import TemplateView, ListView
# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing_page.html"
    
#FUUNCTION BASE VIEW

# def landing_page(request):
#     return render(request, 'landing_page.html')


class LeadListView(ListView):
    
    template_name = "leads/lead_home.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"



# def lead_list(request):
#     leads = Lead.objects.all()

#     context = {
#         "leads": leads,
#     }
#     return render(request, 'leads/lead_home.html', context)

class LeadDetailView(DetailView):
    template_name = "leads/lead_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

#FUUNCTION BASE VIEW
# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }
#     return render(request, 'leads/lead_details.html', context)


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

# ======================class base view lead===================
class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead_list")
    
    def form_valid(self, form):
        # TODO send mail
        send_mail(
            subject="A lead has been created",
            message="Go to the side and see the new leads",
            from_email="test@gmail.com",
            recipient_list = ["greyjoy@gmail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             # first_name = form.cleaned_data['first_name']
#             # last_name = form.cleaned_data['last_name']
#             # age = form.cleaned_data['age']
#             # agent = form.cleaned_data['agent']
            
#             # create the lead to the database
#             # Lead.objects.create(
#             #     first_name=first_name,
#             #     last_name=last_name,
#             #     age=age,
#             #     agent=agent
#             # )
#             form.save()
#             # redirect back to the lead list
#             return redirect('/leads/lead_list')
#     context = {
#         "form": form
#     }
#     return render(request, 'leads/lead_create.html', context)

#===============================class base view for update========================================
class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead_list")

#BEST WAY OF UPDATING
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk) # specific lead we want to update
#     form = LeadModelForm(instance=lead) # form we want to edit
    
#     # check request if it post
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads/lead_list')
#     context = {
#         "form" : form,
#         "lead" : lead
#     }
#     return render(request, 'leads/lead_update.html', context)


# OLD WAY OF UPDATING A LEAD
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = form.cleaned_data['agent']
            
#             # Replacing the old file with the current file gotten form the post data
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.agent = agent
            
#             # save the lead
#             lead.save()
#             # redirect the after submitting to lead list
#             return redirect('/leads/lead_list')
            
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, 'leads/lead_update.html', context)

#====================CLASS BASE DELETE VIEW==================
class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead_list")
    
# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads/lead_list')