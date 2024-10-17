from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm



class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'
    context_object_name = 'agents'
    
    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agents_create.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agents_list')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.oragisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView,self).form_valid(form)
    

    
class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agents_detail.html'
    queryset = Agent.objects.all()
    context_object_name = 'agent'



class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agents_update.html'
    form_class = AgentModelForm
    queryset = Agent.objects.all()
    
    def get_success_url(self):
        return reverse('agents:agents_list')
    

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agents_delete.html'
    queryset = Agent.objects.all()
    
    def get_success_url(self):
        return reverse('agents:agents_list')