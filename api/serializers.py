from rest_framework import serializers
from sonun.models import *
from orders.models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class BaseProduct():
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required= True)
    slug = serializers.SlugField(required= True)

class ReqursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent(value, context = self.context)
        return serializer.data

class ProductSerializer(serializers.ModelSerializer):
    # size = ReqursiveSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        

