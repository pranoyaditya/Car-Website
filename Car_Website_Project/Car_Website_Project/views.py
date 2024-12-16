from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from Car_App.models import Brand

# Class based views are written below.
class HomeView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch all Brand objects from the database
        context['brands'] = Brand.objects.all()  # Make sure 'brands' is passed to the template
        
        return context