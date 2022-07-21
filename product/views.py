import imp
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .schema import ProductSchema
from .models import Product
from .serializer import ProductSerializer


# function views
# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# # @api_view(('GET',))
# # @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# # def all_products(request):
# #     products=Product.objects.all()

# #     serializer=ProductSerializer(data=products,many=True)
# #     if serializer.is_valid():
# #         return Response(serializer.data,status=200)
# #     return Response(serializer.errors,status=400)
    

# class views
class ProductView(APIView):

    """
    List and detail view for the product
    """

    schema=ProductSchema()

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_product(self,request):
        product_id=request.data.get("product_id")
        product=Product.objects.get(id=product_id)
        if product:
            return product
        else:
            return None


    def get(self,request):
        product=self.get_product(request)

        if product:
            serializer=ProductSerializer(product).data
            return Response(serializer,status=200)
        return Response(serializer.errors,status=404)

    def post(self,request):
            serializer=ProductSerializer(data=request.data)

            if serializer.is_valid():
                product=serializer.save()
                return Response(product,status=201)

            return Response(serializer.errors,status=400)

    def put(self,request):
        product=self.get_product(request)

        if product:
            if request.data.get("name"):
                product.name=request.data.get("name")
            if request.data.get("price"):
                product.price=request.data.get("price")
            if request.data.get("description"):
                product.description=request.data.get("description")    

        serializer=ProductSerializer(data=product)
        if serializer.is_valid():
            product=serializer.save()
            return Response(product,status=201)

        return Response(serializer.errors,status=400)


    def delete(self,request):
        product=self.get_product(request)

        if product:
            product.delete()
            return Response(status=200)



