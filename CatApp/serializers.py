from rest_framework import serializers
from .models import CatShop

class CatShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatShop
        fields = (
        'id',
        'name',
        'price',
        'breed',
        'description',
        )

#seriallized the attribute of the model for the view