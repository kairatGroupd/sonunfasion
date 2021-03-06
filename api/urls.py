from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')
router.register('category', views.CategoryViewSet)
router.register('stock', views.StockViewSet)
router.register('size', views.SizeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order/', views.OrderView.as_view())
]