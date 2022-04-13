# Rest Framework
import email
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Models
from apps.profiles.models import User
# Serializers
from apps.profiles.api.serializers import UserSerializer, UserListSerializer, UserUpdateSerializer

""" Creacion de la clase UserAPIView """
# class userAPIView(APIView):

#     def get(self, request):
#         users = User.objects.all()
#         user_serializer = UserSerializer(users, many=True)
#         return Response(user_serializer.data)

""" Creacion de funcion para obtener todos los usuarios """
@api_view(['GET', 'POST'])
def users_api_view(request):
    
    # List
    if request.method == 'GET':
        """ Obtener todos los usuarios """
        # Queryset
        users = User.objects.all()
        users_serializer = UserListSerializer(users, many=True)
    
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    
    # Create
    elif request.method == 'POST':
        """ Crear un nuevo usuario """
        user_serializer = UserSerializer(data=request.data)
        
        # Validate data
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Created User', 'User':user_serializer.data}, status = status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):

    user = User.objects.filter(id=pk).first()

    # Validation
    if user:
        

        # Retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)

        # Update
        elif request.method == 'PUT':
            user_serializer = UserUpdateSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'message':'Updated User {} Successful'.format(user_serializer.data['name'])}, status = status.HTTP_200_OK)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'User Deleted Successful'}, status = status.HTTP_200_OK)

    return Response({'message':'User not found'}, status = status.HTTP_404_NOT_FOUND)