from django.urls import path


from .views import ProductView

urlpatterns=[
    # path('',all_products,name="products"),
    path('',ProductView.as_view(),name="product"),
]