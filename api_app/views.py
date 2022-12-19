from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from .serializer import ProductSerializer, Product2Serializer
from rest_framework import generics


# Create your views here.

def first_api_view(request):
    data={
        "name":"Tobi",
        "profesion":"software developer"
    }
    return Response(data)

@api_view(['GET'])
def second_api_view(request):
    if request.method == 'GET':
        produt=Product.objects.get(id=1)
        if product:
            data=model_to_dict(product)
   
    # get a model instance
    product=Product.objects.get(id=1)
    # data={}
    if product:
        data=model_to_dict(product)
        # data['name']=product.name
        # data['description']=product.description
        # data['price']=product.price
    return Response(data)

@api_view(['GET', 'POST'])
def get_all_product(request):
    if request.method == 'GET':
        all_produt=Product.objects.all()
        serializer=ProductSerializer(all_produt, many=True)
           
    elif request.method == 'POST':
        data=request.data
        serializer=Product2Serializer(data=data)
        serializer.is_valid()
        serializer.save()
        
    # all_product=Product.objects.all()
    # serializer=ProductSerializer(all_product, many=True)
  
        return Response(serializer.data, status=201)
    return Response(serializer.data, status=200)


class GetAllProductView(APIView):
    def get(self, request, *args, **kwargs):
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GetProductCategoryView(APIView):
#     def get(self, request, cat):
#         products=Product.objects.filter(category=cat)
#         serializer=ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class GetProductCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        cate=kwargs.get('category')
        products=Product.objects.filter(category=cate)
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    def get_objects(self, pk):
        try:
            product=Product.objects.get(id=pk)
            return product
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        product=self.get_objects(kwargs.get('pk'))
        serializer=ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

        # UPDATE
    def put(self, request, pk):
        product=self.get_objects(pk)
        serializer=ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_RE)

    def delete(self, request, pk):
        product=self.get_objects(pk)
        product.delete()
        return Response({'message':'item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# generic api views
class AllProductView(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def get_queryset(self):
        queryset=self.queryset.filter(name__istartswith='t')
        return queryset


class AllProductCreateView(generics.ListCreateAPIView):
    user='admin'
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def perform_create(self, serializer):
        print(serializer)
        if self.user != 'admin':
            raise ValidationError('only admin can add new product')
        serailizer.save()
        send_user_email


class GetAllProductView(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

# class AllProductCreateView(generics.ListCreateAPIView):
#     serializer_class=ProductSerializer
#     queryset=Product.objects.all()

class ProductDetail2(generics.RetrieveAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class DeleteProduct(generics.DestroyAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()







