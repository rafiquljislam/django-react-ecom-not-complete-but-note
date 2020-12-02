from django.urls import path,include
from .views import  *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('catagorys', CatagoryAPIView, basename='catagorys')
router.register('products', ProductAPIView, basename='products')
router.register('cart', CartAPIView, basename='cart')
router.register('cartproducts', CartProductAPIView, basename='cartproducts')
router.register('order', OrderAPIView, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('customer/', CustomerAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('login/',obtain_auth_token),
    path('register/', UserViewSet.as_view()),
]
