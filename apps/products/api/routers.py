from rest_framework.routers import DefaultRouter
from apps.products.api.views.products_viewsets import ProductViewSet
from apps.products.api.views.general_views import CategoriesViewSet

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoriesViewSet, basename='categories')

urlpatterns = router.urls