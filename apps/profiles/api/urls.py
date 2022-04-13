from django.urls import path
from apps.profiles.api.api import user_detail_view, users_api_view, users_api_view

urlpatterns = [
    # path('', userAPIView.as_view(), name='users_api'),
    path('users/', users_api_view, name='users_api'),
    path('users/<int:pk>/', user_detail_view, name='users_detail_api'),
]