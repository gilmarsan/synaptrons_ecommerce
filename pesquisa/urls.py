from django.urls import path

app_name = "pesquisa"

from .views import(
    PesquisaProductView,
)
urlpatterns = [
    path('', PesquisaProductView.as_view(), name='query'),
]
