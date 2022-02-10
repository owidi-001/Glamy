from django.urls import path
from .views import AdminCategoryView,AdminProductsView,ClientCategoryView,ClientProductsView

app_name="store"

urlpatterns = [
    path('admin/category', AdminCategoryView.as_view(),name="admin_category"),
    path('admin/products', AdminProductsView.as_view(),name="admin_product"),
    path('client/category', ClientCategoryView.as_view(),name="clint_category"),
    path('client/products', ClientProductsView.as_view(),name="clint_product"),
]
