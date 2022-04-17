from rest_framework import serializers
from apps.products.models import Category, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('state','modified_date','created_date', 'inactivation_date')

class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        exclude = ('state','modified_date', 'inactivation_date',)
    
    def to_representation(self, instance):
        if instance.image_upload:
            obj = {
                'image': instance.image_upload
            }
        elif instance.image_url:
            obj = {
                'image': instance.image_url
            }
        else:
            obj = {
                'image': instance.image_upload,
                'image': instance.image_url
            }
        return obj