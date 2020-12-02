from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.http import JsonResponse
import json

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customerimage/',default="default.png")

    def __str__(self):
        return self.user.username
    
class Catagory(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',unique_with=['pub_date__month'])

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',unique_with=['pub_date__month'])
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/",blank=True, null=True)
    marcked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=300, blank=True, null=True)
    return_policy = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.title

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)
    credted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart " + str(self.id)

    def CartProd(self):
        
        return json.dumps(CartProduct.objects.filter(cart=self))

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
    ("Esewa", "Esewa"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)
