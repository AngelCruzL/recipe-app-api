"""
Serializers for the recipe API
"""
from core.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for the recipe object"""

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'time_in_minutes',
            'price',
            'link'
        ]
        read_only_fields = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for the recipe detail view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
