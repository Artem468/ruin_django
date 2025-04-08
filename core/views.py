from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view

from core.models import Tour, Point
from core.serializers import TourSerializer, PointSerializer


def front(request, *args, **kwargs):
    return render(request, "index.html")


@api_view(['GET'])
def get_tours(request):
    try:
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return JsonResponse({
            "status": "ok",
            "data": serializer.data,
            "message": None
        })
    except Exception as err:
        return JsonResponse({
            "status": "error",
            "data": [],
            "message": err
        })


@api_view(['GET'])
def get_tour_by_id(request, tour_id):
    try:
        tour = Tour.objects.get(id=tour_id)
        serializer = TourSerializer(tour)
        return JsonResponse({
            "status": "ok",
            "data": serializer.data,
            "message": None
        })
    except Exception as err:
        return JsonResponse({
            "status": "error",
            "data": None,
            "message": err
        })


@api_view(['GET'])
def get_tour_points(request, tour_id):
    try:
        points = Point.objects.filter(tour_id=tour_id)
        serializer = PointSerializer(points, many=True)
        return JsonResponse({
            "status": "ok",
            "data": serializer.data,
            "message": None
        })
    except Exception as err:
        return JsonResponse({
            "status": "error",
            "data": [],
            "message": err
        })
