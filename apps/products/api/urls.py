from django.urls import path
from apps.products.api.views.general_views import CategoryListAPIView
from apps.products.api.views.products_views import (
        ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    )

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    # path('products/destroy/<int:pk>/', ProductDstroyAPIView.as_view()),
    # path('products/update/<int:pk>/', ProductUpdateAPIView.as_view()),
]