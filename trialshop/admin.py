from django.contrib import admin
from trialshop.models import Product,catagory,Cart
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","product_type","product_name","product_brand","pub_date","product_price","cart_value","product_pic","product_pic_name","product_detail"]
    search_fields = ["product_name"]
    fieldsets = [
        (None,               {'fields':["product_type","product_name","product_brand","product_price","cart_value","product_pic","product_detail"]}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_filter = ["product_type"]

admin.site.register(Product, ProductAdmin)
admin.site.register(catagory)
admin.site.register(Cart)



'''class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields':["product_type","product_name","product_brand","product_price","cart_value","product_pic","product_pic_name"]}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    list_filter = ['pub_date']
    search_fields=['product_name']
    
admin.site.register(Product, ProductAdmin)
'''