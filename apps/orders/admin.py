from django.contrib import admin
from apps.orders.models import OrderDetail, Order

# Register your models here.


@admin.register(OrderDetail)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('product', 'quantity', 'unit_price', 'subtotal')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ['product',]
    # date_hierarchy = ''
    # ordering = ('',)

class OrderDetailInline(admin.TabularInline):
    '''Stacked Inline View for OrderDetail'''

    model = OrderDetail
    extra = 0
    raw_id_fields = ('product',)
    autocomplete_fields = ('product',)
    fieldsets = (
        (None, {
            'fields': (('product', 'quantity',), (
                ))
        }),)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ('profile', 'total', 'get_total')
    # list_filter = ('',)
    inlines = [
        OrderDetailInline,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
