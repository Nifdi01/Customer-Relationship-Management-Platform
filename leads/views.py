from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadModelForm, CustomUserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class SignUpView(CreateView):
    template_name="registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin, ListView):
    template_name="leads/lead_list.html"
    queryset=Lead.objects.all()
    context_object_name="leads"


class LeadDetailView(DetailView):
    template_name="leads/lead_detail.html"
    queryset=Lead.objects.all()
    context_object_name="lead"


class LeadCreateView(CreateView):
    template_name="leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list = ["test2@test.com"]
        )

        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(UpdateView):
    template_name="leads/lead_update.html"
    queryset=Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(DeleteView):
    template_name="leads/lead_delete.html"
    queryset=Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")