from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class PesquisaProductView(ListView):
    template_name = "pesquisa/views.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kargs):
        request = self.request
        result = request.GET
        query = result.get('q', None) # result['q']
        if query is not None:
            return Product.objects.filter(title__icontains = query)
        return Product.objects.featured()
