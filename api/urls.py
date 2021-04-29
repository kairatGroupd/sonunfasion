from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
# router.register('orders', views.OrderViewSet)
router.register('stock', views.StockViewSet)
router.register('order', views.OrderViewset)
# router.register('order_item', views.OrderItemViewset)
router.register('size', views.SizeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]