from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def director_list_api_view(request):
    dict_ = {
        "text": 'Christopher Nolan, ...',
        "int": 100,
        "float": 3.14,
        "bool": True,
        "list": [1, 2, 3],
        "dict": {"a": 1, "b": 2}
    }
    return Response(data={}, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_list_api_view(request):
    dict_ = {
        "text": 'Interstellar, Batman, ...',
        "int": 100,
        "float": 3.14,
        "bool": True,
        "list": [1, 2, 3],
        "dict": {"a": 1, "b": 2}
    }
    return Response(data={}, status=status.HTTP_200_OK)


@api_view(['GET'])
def reviews_list_api_view(request):
    return Response(data={}, status=status.HTTP_200_OK)
