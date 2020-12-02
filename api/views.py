from rest_framework.views import  APIView
from .serializers import *
from ecom.models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet,ViewSet
from django.shortcuts import get_object_or_404,Http404
from rest_framework import status

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def get(self, request):
        serializer = User_Serializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = User_Serializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,  status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def get(self, request):
        user = request.user.id
        profile = Customer.objects.get(id=user)
        serializer = Profile_serializers(profile)
        return Response(serializer.data)

    def put(self, request):
        user = request.user.id
        profile = Customer.objects.get(user=user)
        serializer = Profile_serializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,  status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatagoryAPIView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = Catagory_serializers
    queryset = Catagory.objects.all()

class ProductAPIView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = Product_serializers
    queryset = Product.objects.all()





class CartAPIView(ViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def list(self, request):
        user=request.user
        # queryset = Cart.objects.filter(customer=Customer.objects.get(user=user))
        queryset = Cart.objects.filter(customer__user=user)
        serializer = Cart_serializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user=request.user
        customer = Customer.objects.get(user=user)
        serializer = Cart_serializers(data=request.data)
        if serializer.is_valid():
            customer = customer
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk=None):
        user=request.user
        queryset = Cart.objects.filter(customer=Customer.objects.get(user=user))
        artical = get_object_or_404(queryset, pk=pk)
        serializer = Cart_serializers(artical)
        return Response(serializer.data)

    def update(self, request,pk=None):
        user=request.user
        queryset = Cart.objects.filter(customer=Customer.objects.get(user=user))
        artical = get_object_or_404(queryset, pk=pk)
        serializer = Cart_serializers(artical,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request,pk=None, *args, **kwargs):
        user=request.user
        queryset = Cart.objects.filter(customer=Customer.objects.get(user=user))
        try:
            artical = get_object_or_404(queryset, pk=pk).delete()
            return  Response({"Success": "Delate Successfully"})
        except Http404:
            pass
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartProductAPIView(ViewSet):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    
    def list(self, request):
        user=request.user
        queryset = CartProduct.objects.filter(cart__customer__user=user)
        serializer = CartProduct_serializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        user=request.user
        queryset = CartProduct.objects.filter(cart__customer__user=user)
        article = get_object_or_404(queryset, pk=pk)
        serializer = CartProduct_serializers(article)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CartProduct_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        user=request.user
        queryset = CartProduct.objects.filter(cart__customer__user=user)
        artical = get_object_or_404(queryset, pk=pk)
        print(artical)
        serializer = CartProduct_serializers(artical,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,pk=None, *args, **kwargs):
        user=request.user
        queryset = CartProduct.objects.filter(cart__customer__user=user)
        try:
            artical = get_object_or_404(queryset, pk=pk).delete()
            return  Response({"Success": "Delate Successfully"})
        except Http404:
            pass
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderAPIView(ViewSet):
    permission_classes = [IsAuthenticated, ]

    def list(self, request):
        user=request.user
        queryset = Order.objects.filter(cart__customer__user=user)
        serializer = Order_serializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        user=request.user
        queryset = Order.objects.filter(cart__customer__user=user)
        article = get_object_or_404(queryset, pk=pk)
        serializer = Order_serializers(article)
        return Response(serializer.data)

    def destroy(self, request,pk=None, *args, **kwargs):
        user=request.user
        queryset = Order.objects.filter(cart__customer__user=user)
        try:
            artical = get_object_or_404(queryset, pk=pk).delete()
            return  Response({"Success": "Delate Successfully"})
        except Http404:
            pass
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(APIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,  status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
