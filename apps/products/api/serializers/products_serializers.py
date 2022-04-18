
from rest_framework import serializers
from apps.products.api.serializers.general_serializers import CategorySerializer, ProductImageSerializer
from apps.products.models import Product, ProductImage, Category

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state','modified_date', 'inactivation_date', 'created_date',)


    def to_representation(self, instance):
        obj = {
                "id": instance.id,
                "name": instance.name,
                "description": instance.description,
                "stock": instance.stock,
                "images": instance.get_images(),
                "price": instance.price,
                "total_descount": instance.total_descount(),
                "category": instance.category.description if instance.category is not None else '',
                "descount": instance.descount,
            }
        return obj


class ProductCreateSerializer(serializers.ModelSerializer):
    # images = ProductImageSerializer(many=True)
    images = serializers.ListField()

    class Meta:
        model = Product
        exclude = ('state','modified_date', 'inactivation_date', 'created_date',)
    
    def create(self, validated_data):
        # Extract images and save a list of images
        images_data = validated_data.pop('images')
        # Create a product for last can create the images
        product = Product.objects.create(**validated_data)
        # Get a image in the list and create one a one for product
        for image in images_data:
            print(image)
            ProductImage.objects.create(product=product, image_url=image)
        return product

class ProductUpdateSerializer(serializers.ModelSerializer):
    # images = ProductImageSerializer(source='image_product', many=True)
    images = serializers.ListField()

    class Meta:
        model = Product
        exclude = ('state','modified_date', 'inactivation_date', 'created_date',)

    def to_representation(self, instance):
        obj = {
                "id": instance.id,
                "name": instance.name,
                "description": instance.description,
                "stock": instance.stock,
                "images": instance.get_images(),
                "price": instance.price,
                "total_descount": instance.total_descount(),
                "category": instance.category.description if instance.category is not None else '',
                "descount": instance.descount,
            }
        return obj


    def update(self, instance, validated_data):
        if validated_data.get('images'):
            # Extract images send in the Json an save a list
            images_data = validated_data.pop('images')
            # Get a image an check the image exists in DB
            for image in images_data:
                print(image)
                if not ProductImage.objects.filter(image_url=image):
                    ProductImage.objects.create(product=instance, image_url=image)       
        update_product = super().update(instance, validated_data)
        update_product.save()
        return update_product