from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from Car_App.models import Brand,Car

# Class based views are written below.
class HomeView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand_id = self.kwargs.get('brand_id',None)

        if brand_id:
            brand = Brand.objects.get(id = brand_id)
            context['selected_brand'] = brand
            context['cars'] = Car.objects.filter(brand = brand)
        else:
            context['selected_brand'] = None
            context['cars'] = Car.objects.all()

        context['brands'] = Brand.objects.all()
        
        return context