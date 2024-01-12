from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorSerializer, MovieSerializer, ReviewsSerializer, DirectorValidateSerializer, \
    MovieValidateSerializer, ReviewValidateSerializer
from .models import Director, Movie, Review


@api_view(['GET', 'POST', 'DELETE'])
def director_list_api_view(request, id):
    if request.method == 'GET':

        director = Director.objects.select_related(
            'movie'
        ).prefetch_related(
            'reviews'
        ).all()

        serializer = DirectorSerializer(director, many=True)

        return Response(data=serializer.data)
    else:
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')

        director = Director.objects.create(name=name, description=description)
        director.save()

        return Response(data={'id': director.id}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_list_api_view(request):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        movie.name = request.data.get('name')
        movie.description = request.data.get('description')
        movie.save()
        return Response(data={'id': movie.id}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')

    return Response(data={'id': movie.id}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def reviews_list_api_view(request):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewsSerializer(reviews)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        reviews.name = request.data.get('name')
        reviews.description = request.data.get('description')
        reviews.save()
        return Response(data={'id': reviews.id}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')

    return Response(data={'id': reviews.id}, status=status.HTTP_201_CREATED)
