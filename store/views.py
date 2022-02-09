from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
# Documentation schema
from .schema import *
from .serializers import ProductSerializer


"""
The vendors and admin panel
Where all product and category CRUD goes
"""
@method_decorator(csrf_exempt, name="dispatch")
class ProductsView(APIView):
    schema = ProductSchema()

    permission_classes = (IsAuthenticated,)

    """
        Return all products
    """

    def get(self, request):
        query = Product.objects.all()
        response = ProductSerializer(query, many=True).data

        return Response(response)

    """
        Save a product
    """

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(commit=False)
            serializer.created_by = request.user
            serializer.save(request, )
            return Response(serializer, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request):
        """
            Update product price
        """
        product_id = request.data.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        product.price = request.data.get("Price")
        product.save()

        return Response(ProductSerializer(product).data, status=200)

    def delete(self, request):
        """
        Remove product
        """
        product_id = request.data.get("product_id")
        product = get_object_or_404(Product, product_id)
        product.delete()

        return Response(ProductSerializer(product), status=301)
