from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead, Agent
from .forms import LeadModelForm, CustomUserCreationForm
from django.views import generic  

 

class LeadsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/home.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'




class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'
    



class LeadsCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    
    def get_success_url(self):
       return reverse('leads:lead_view')
   
    def form_valid(self, form):
        send_mail(
            subject="a new Lead has been createt",
            message='Gute Arbeit! Sie dir das Lead auf der Homepage an',
            from_email='ssc_consult@outlook.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadsCreateView,self).form_valid(form)
    
    
    

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse('leads:lead_view')




class SignUpView(generic.CreateView):
    template_name = 'registration/signUp.html'
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
       return reverse('login')
   



def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return reverse('leads:lead_view')
