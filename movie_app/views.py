from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from movie_app.serializers import DirectorSerializer, MovierSerializer, ReviewSerializer, DirectorValidateSerializer, \
    MovieValidateSerializer, ReviewValidateSerializer


from movie_app.models import Director, Movie, Review


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == "GET":
        print(request.user)
        director = Director.objects.all()
        data = DirectorSerializer(instance=director, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400, data=serializer.errors)
        name = serializer.validated_data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data=DirectorSerializer(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response(data={'message': 'Directors object does not exists!'}, status=404)
    if request.method == "GET":
        data = DirectorSerializer(instance=director, many=False).data
        return Response(data=data)
    elif request.method == "PUT":
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)
    else:
        director.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == "GET":
        print(request.user)
        movie = Movie.objects.all()
        data = MovierSerializer(instance=movie, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400, data=serializer.errors)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.create(
            title=title, description=description,
            director_id=director_id,  duration=duration
        )
        movie.save()
        return Response(data=MovierSerializer(movie).data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, movies_id):
    try:
        movie = Movie.objects.get(id=movies_id)
    except Movie.DoesNotExist:
        return Response(data={'message': 'Movies object does not exists!'}, status=404)
    if request.method == 'GET':
        data = MovierSerializer(instance=movie, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        return Response(data=MovierSerializer(movie).data)
    else:
        movie.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == "GET":
        print(request.user)
        review = Review.objects.all()
        serializer = ReviewSerializer(instance=review, many=True)
        total_reviews = Review.objects.count()
        total_stars = Review.objects.aggregate(total_stars=Sum('stars'))['total_stars']
        overall_average_rating = total_stars / total_reviews if total_reviews > 0 else 0

        overall_average_rating = round(overall_average_rating, 3)
        data = {
            'reviews': serializer.data,
            'rating': overall_average_rating,
        }
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400, data=serializer.errors)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        review = Review.objects.create(
            text=text, movie_id=movie_id,
            stars=stars
        )
        review.save()
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Reviews object does not exists!'},
                        status=404)
    if request.method == "GET":
        data = DirectorSerializer(instance=review, many=False).data
        return Response(data=data)
    elif request.method == "PUT":
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)
    else:
        review.delete()
        return Response(status=204)


