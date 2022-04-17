from django.contrib import admin
from apps.products.models import Category, ProductImage, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('id','description', 'state')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('description',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    '''Admin View for ProductImage'''

    list_display = ('product', 'image_upload', 'image_url',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = (
        'name', 'description', 'category', 'price', 
        'stock', 'is_off', 'total_descount', 'state'
        )
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
