from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.core.api import GeneralListAPIView
from apps.products.models import Category, ProductImage
from apps.products.api.serializers.general_serializers import CategorySerializer, ProductImageSerializer    


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return self.get_serializer_class().Meta.model.objects.filter(state=True)
        return self.get_serializer_class().Meta.model.objects.filter(id=pk, state=True).first()

    def destroy(self, request, pk=None):
        category = self.get_queryset().filter(id=pk).first()
        if category:
            category.state = False
            category.save()
            return Response({'message': 'Product Destroy Successful'}, status=status.HTTP_200_OK)
        
        return Response({'message': 'This Product No Exists'}, status=status.HTTP_400_BAD_REQUEST)

# class CategoryListAPIView(GeneralListAPIView):
#     serializer_class = CategorySerializer