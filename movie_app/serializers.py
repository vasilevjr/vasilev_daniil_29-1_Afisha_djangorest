from rest_framework import serializers
from django.db.models import Count
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError
class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, director):
        return director.movies.count()


class MovierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title duration director'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=100)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=150)
    description = serializers.CharField(required=False)
    duration = serializers.FloatField(required=True)
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Category does not exists!')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    stars = serializers.IntegerField(required=True, min_value=1, max_value=5)
    movie_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Category does not exists!')
        return movie_id
