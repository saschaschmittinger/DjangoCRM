from django.shortcuts import render,redirect
from .models import Lead, Agent
from .forms import LeadForm
from django.views.generic import ListView, DetailView
 


class LeadListView(ListView):
    template_name = 'leads/home.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'



class LeadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'



def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect("/leads")



def lead_create(request):
    form = LeadForm()
    title = 'create leads'
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']  
            age = form.cleaned_data['age']   
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect("/leads") 
    
    context ={
        'title':title,
        'form':form
    }
    return render(request, 'leads/lead_create.html', context) 



def lead_update(request, pk):
    title = 'update lead'
    lead = Lead.objects.get(id=pk)
    form = LeadForm(request.POST)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']  
            age = form.cleaned_data['age']       
            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age
            lead.save()
            
            return redirect("/leads") 
    context = {
        'lead':lead,
        'title':title,
        'form':form
    }
    return render(request, 'leads/lead_update.html',context)

