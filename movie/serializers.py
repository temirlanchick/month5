from rest_framework import serializers

from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text rating created_at'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255, min_length=3)
    description = serializers.CharField(required=False)


class MovieValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255, min_length=3)
    description = serializers.CharField(required=False)


class ReviewValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255, min_length=3)
    description = serializers.CharField(required=False)
