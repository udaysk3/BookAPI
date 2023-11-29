from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PartialBookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Replace with your actual model
        fields = ['title', 'author', 'publication_year']

    title = serializers.CharField(required=False, max_length=255)
    author = serializers.CharField(required=False, max_length=255)
    publication_year = serializers.IntegerField(required=False)

    def validate(self, data):
        # Perform custom validation for specific fields
        if 'title' in data and len(data['title']) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        if 'publication_year' in data and data['publication_year'] < 1000:
            raise serializers.ValidationError("Publication year must be greater than 1000.")
        return data

# serializers.py
from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    