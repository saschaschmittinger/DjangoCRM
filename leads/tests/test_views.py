from django.test import TestCase
from django.urls import reverse


class LeadListViewTest(TestCase):
    
    def test_get(self):
        response = self.client.get(reverse('leads:lead_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leads/home.html')
        

 