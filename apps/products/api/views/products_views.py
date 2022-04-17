from apps.products.models import Product
from rest_framework import generics, status
from rest_framework.response import Response
from apps.core.api import GeneralListAPIView
from apps.products.api.serializers.products_serializers import (
    ProductListSerializer, ProductCreateSerializer, ProductUpdateSerializer
    )


# List All Products
class ProductListAPIView(GeneralListAPIView):
    """
    List all products, or create a new product.
    """
    serializer_class = ProductListSerializer


# Create a New Product and Images
class ProductListCreateAPIView(generics.ListCreateAPIView):
    """ List all products, or create a new product. """
    serializer_class = ProductCreateSerializer
    queryset = ProductCreateSerializer.Meta.model.objects.filter(state=True)

    def get(self, request):
        products = Product.objects.all().filter(state=True)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Send the data to serializer
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product Created Successful'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View Detail a one Product
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductUpdateSerializer

    def get_queryset(self, pk=None):
        return self.get_serializer_class().Meta.model.objects.filter(state=True)

    # Logic Destroy
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product Destroy Successful'}, status=status.HTTP_200_OK)
        
        return Response({'message': 'This Product No Exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Logic Patch
    def patch(self, request, pk=None):
        product = ProductListSerializer.Meta.model.objects.filter(state=True).filter(id=pk).first()
        if product:
            product_serializer = ProductListSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        Response({'message': 'This Product No Exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Logic Put
    def put(self, request, pk=None):
        product = ProductListSerializer.Meta.model.objects.filter(state=True).filter(id=pk).first()
        if product:
            product_serializer = ProductUpdateSerializer( product, data=request.data, context=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Logical Delete a Product change state to False
# class ProductDstroyAPIView(generics.DestroyAPIView):
#     serializer_class = ProductListSerializer

#     def get_queryset(self):
#         return self.get_serializer_class().Meta.model.objects.filter(state=True)
    
#     # Logic Destroy
#     def delete(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message': 'Product Destroy Successful'}, status=status.HTTP_200_OK)
        
#         return Response({'message': 'This Product No Exists'}, status=status.HTTP_400_BAD_REQUEST)


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductUpdateSerializer

#     def get_queryset(self, pk):
#         return self.get_serializer_class().Meta.model.objects.filter(state=True).filter(id=pk).first()
    
#     def patch(self, request, pk=None):
#         if self.get_queryset(pk):
#             product_serializer = ProductListSerializer(self.get_queryset(pk))
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         Response({'message': 'This Product No Exists'}, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, pk=None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data, context=request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response(product_serializer.data, status=status.HTTP_200_OK)
#             return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)