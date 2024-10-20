from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisatorAndLoginRequiredMixin



class AgentListView(OrganisatorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'
    context_object_name = 'agents'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    

class AgentCreateView(OrganisatorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agents_create.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agents_list')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.oragisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView,self).form_valid(form)
    

    
class AgentDetailView(OrganisatorAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agents_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    


class AgentUpdateView(OrganisatorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agents_update.html'
    form_class = AgentModelForm
     
    def get_success_url(self):
        return reverse('agents:agents_list')
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    


class AgentDeleteView(OrganisatorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agents_delete.html'
       
    def get_success_url(self):
        return reverse('agents:agents_list')
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)