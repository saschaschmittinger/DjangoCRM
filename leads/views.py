from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Lead, Agent
from .forms import LeadModelForm
from django.views import generic  


 

class LeadsListView(generic.ListView):
    template_name = 'leads/home.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'



class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
    


class LeadsCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    
    def get_success_url(self):
       return '/leads'
    
    

class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return '/leads'



def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect("/leads")



