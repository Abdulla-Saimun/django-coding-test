from django.contrib import admin
from .models import Product, Variant, ProductVariant, ProductVariantPrice

# Register your models here.
class ProductAAdmin(admin.ModelAdmin):
    list_display = ("title", "sku", "description")


class VariantAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "active")


class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("variant_title", "variant", "product")


class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = (
        "product_variant_one",
        "product_variant_two",
        "product_variant_three",
        "price",
        "stock",
        "product",
    )


admin.site.register(Product, ProductAAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(ProductVariantPrice, ProductVariantPriceAdmin)
