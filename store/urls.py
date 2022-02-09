from django.urls import path
from .views import ProductsView

urlpatterns = [
    path('store/', ProductsView.as_view())
]
