from rest_framework import  serializers
from ecom.models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import json

User = get_user_model()
class User_Serializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['id','username','first_name','last_name','email','date_joined']


class Profile_serializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class Catagory_serializers(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'

class Product_serializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

class CartProduct_serializers(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'
        depth = 1


class Cart_serializers(serializers.ModelSerializer):
    # CartProd = CartProduct_serializers('CartProd')
    # def get_filtered_data(self, obj):
    #     serelizer=CartProduct_serializers(CartProd, many=True )
    #     return serelizer.data
    class Meta:
        model = Cart # 'CartProd'
        fields = ['id','customer','total','credted_at','CartProd']
        depth = 1



class Order_serializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user