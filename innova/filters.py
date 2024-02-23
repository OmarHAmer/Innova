import django_filters
from .models import *




class ProductsFilter(django_filters.FilterSet):
    
    product_category = django_filters.NumberFilter(field_name='product_category')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Products
        fields = [
            'product_category',
            'name',
            'description',
        ]