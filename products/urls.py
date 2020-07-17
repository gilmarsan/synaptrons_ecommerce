from django.urls import path

from .views import (
                        ProductListView,
                        ProductDetailSlugView,
                    )

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug:slug>/', ProductDetailSlugVieww.as_view())
]
