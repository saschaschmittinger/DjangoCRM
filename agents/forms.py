from django import forms
from leads.models import Agent


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'        