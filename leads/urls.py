from django.urls import path
from .views import *

app_name = 'leads'

urlpatterns =[
    path('', LeadsListView.as_view(), name='lead_view'),
    path('<int:pk>/',LeadDetailView.as_view(), name='lead_detail'),
    path('<int:pk>/update/',LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/',LeadDeleteView.as_view(), name='lead_delete'),
    path('create/', LeadsCreateView.as_view(), name='lead_create'),
 
]
