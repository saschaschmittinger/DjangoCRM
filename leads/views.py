from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead, Agent
from .forms import LeadModelForm, CustomUserCreationForm
from django.views import generic


class LeadsListView(LoginRequiredMixin, generic.ListView):
    title = "SSC LeadListView"
    template_name = "leads/home.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

    def get_context_data(self, **kwargs):
        context = super(LeadsListView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    title = "SSC LeadDetailView"
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_context_data(self, **kwargs):
        context = super(LeadDetailView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class LeadsCreateView(LoginRequiredMixin, generic.CreateView):
    title = "SSC LeadCreateView"
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_view")

    def form_valid(self, form):
        send_mail(
            subject="a new Lead has been createt",
            message="Gute Arbeit! Sie dir das Lead auf der Homepage an",
            from_email="ssc_consult@outlook.com",
            recipient_list=["test2@test.com"],
        )
        return super(LeadsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LeadsCreateView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    title = "SSC LeadUpdateView"
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead_view")

    def get_context_data(self, **kwargs):
        context = super(LeadUpdateView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class SignUpView(generic.CreateView):
    title = "SSC SignUpView"
    template_name = "registration/signUp.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context.update({"title": self.title})
        return super().get_context_data(**kwargs)


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead_view")
