from rest_framework import generics
from apps.core.api import GeneralListAPIView
from apps.products.models import Category, ProductImage
from apps.products.api.serializers.general_serializers import CategorySerializer, ProductImageSerializer    

class CategoryListAPIView(GeneralListAPIView):
    serializer_class = CategorySerializer