from django.urls import path

app_name = "pesquisa"

from products.views.import(
    ProductListView,
)
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
]
