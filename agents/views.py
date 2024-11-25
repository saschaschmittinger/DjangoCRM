from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisatorAndLoginRequiredMixin


class AgentListView(OrganisatorAndLoginRequiredMixin, generic.ListView):
    title = "SSC Agents"
    template_name = "agents/agents_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_context_data(self, **kwargs):
        context = super(AgentListView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class AgentCreateView(OrganisatorAndLoginRequiredMixin, generic.CreateView):
    title = "SSC AgentCreateView"
    template_name = "agents/agents_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agents_list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.oragisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AgentCreateView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class AgentDetailView(OrganisatorAndLoginRequiredMixin, generic.DetailView):
    title = "SSC AgentDetailView"
    template_name = "agents/agents_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_context_data(self, **kwargs):
        context = super(AgentDetailView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class AgentUpdateView(OrganisatorAndLoginRequiredMixin, generic.UpdateView):
    title = "SSC AgentUpdateView"
    template_name = "agents/agents_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agents_list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_context_data(self, **kwargs):
        context = super(AgentUpdateView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class AgentDeleteView(OrganisatorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agents_delete.html"

    def get_success_url(self):
        return reverse("agents:agents_list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
