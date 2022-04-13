from rest_framework import serializers
from apps.profiles.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields= '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('email',)

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserUpdateEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)

class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields= [
                'id', 'email', 'name', 
                'last_name', 'profile_img',
                'is_active', 'groups'
                ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'email': data['email'],
            'name': data['name'],
            'last_name': data['last_name'],
            'profile_img': data['profile_img'],
            'is_active': data['is_active'],
            'groups': data['groups'],
            }