import django_filters

from .models import ProductVariantPrice


class ProductFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = ProductVariantPrice
        fields = ["product", "created_at", "product_variant_one"]
