from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializer, MovierSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET'])
def director_list_api_view(request):
    director = Director.objects.all()
    data = DirectorSerializer(instance=director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    movie = Movie.objects.all()
    data = MovierSerializer(instance=movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(instance=review, many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_detail_api_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        return Response(data={'message': 'Directors object does not exists!'}, status=404)
    data = DirectorSerializer(instance=director, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, movies_id):
    try:
        movie = Movie.objects.get(id=movies_id)
    except Movie.DoesNotExist:
        return Response(data={'message': 'Movies object does not exists!'}, status=404)
    data = MovierSerializer(instance=movie, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, review_id):
    try:
        review = Director.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Reviews object does not exists!'}, status=404)
    data = DirectorSerializer(instance=review, many=False).data
    return Response(data=data)