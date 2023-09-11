from rest_framework import serializers

from .models import Document, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'title',
            'position_status',
            'position_location',
            'company_name',
            'created_at_formatted'

        )

class DocumentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'category',
            'title',
            'description',
            'position_status',
            'position_location',
            'company_name',
            'company_location',
            'company_email',
            'created_at_formatted'

        )

