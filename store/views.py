from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .forms import ProductForm, ProductUpdateForm, CategoryForm, CategoryUpdateForm
from .models import Product, Category
# Documentation schema
from .schema import *
from .serializers import ProductSerializer, CategorySerializer
from django.template.defaultfilters import slugify





class AdminCategoryView(APIView):
    """
    Admin category CRUD platform
    """

    schema = CategorySchema()
    permission_classes = (IsAuthenticated, IsAdminUser)

    """
    Admin can query categories available
    """

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)

    """
        Admin can add new category
    """

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(form.data.get("name"))
            category.save()
            serializer = CategorySerializer(category).data

            return Response(serializer, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        form = CategoryUpdateForm(request.data)
        if form.is_valid():
            category_id = request.data.get("category_id")
            category = get_object_or_404(Category, id=category_id)
            category.name = request.data.get("name")
            category.save()
            serializer = CategorySerializer(category).data
            return Response(serializer, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)





class AdminProductsView(APIView):
    """
        The admin panel
        Where all product and category CRUD goes
    """
    schema = ProductSchema()
    permission_classes = (IsAuthenticated, IsAdminUser)

    """
    Return all products in the catalogue to the admin
    """

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer, status=status.HTTP_200_OK)

    """
    Add new product into the catalogue
    """

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.slug = slugify(form.data.get("name"))
            product.save()

            return Response(ProductSerializer(product), status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Update product quantity in stock
    """

    def patch(self, request):
        product_id = request.data.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        if product.in_stock and not product.quantity:
            product.in_stock = False
            product.is_active = False
            product.save()
            serializer = ProductSerializer(product).data
            return Response(serializer, status=status.HTTP_200_OK)

    """
        Update product quantity in stock
    """

    def put(self, request):
        form = ProductUpdateForm(request.POST)
        if form.is_valid():
            product_id = request.data.get("product_id")
            product = get_object_or_404(Product, id=product_id)
            if form.data.get("quantity"):
                product.quantity = form.quantity
            if form.price:
                product.price = form.data.get("price")

            product.save()
            serializer = ProductSerializer(product).data
            return Response(serializer, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        product_id = request.data.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        serializer = ProductSerializer(product).data

        return Response(serializer, status=status.HTTP_200_OK)



class ClientCategoryView(APIView):
    """
        Client browses products by category
        No authentication required
    """
    def get(self,request):
        category_id=request.data.get("category_id")
        category=get_object_or_404(Category,id=category_id)
        serializer=CategorySerializer(category).data
        return Response(serializer,status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name="dispatch")
class ClientProductsView(APIView):
    """
        Returns product details
    """

    schema = ProductSchema()


    def get(self, request):
        product_id=request.data.get("product_id")
        product=get_object_or_404(Product,id=product_id)
        serializer=ProductSerializer(product).data

        return Response(serializer,status=status.HTTP_200_OK)
