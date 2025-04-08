from django.db.models import ExpressionWrapper, F, DurationField
from django.db.models.functions import Greatest
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view

from core.models import Tour, Point, ScheduledTour
from core.serializers import TourSerializer, PointSerializer, EntrySerializer, ScheduledTourWithTourDataSerializer


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
def get_scheduled_tours(request):
    try:
        tours = ScheduledTour.objects.all()
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


@api_view(['GET'])
def get_nearest_tour(request):
    now = timezone.now()

    time_diff_expr = ExpressionWrapper(
        Greatest(F('start_at') - now, now - F('start_at')),
        output_field=DurationField()
    )

    nearest_tour = (
        ScheduledTour.objects.annotate(time_diff=time_diff_expr)
        .order_by('time_diff')
        .first()
    )

    if nearest_tour is None:
        return JsonResponse({
            "status": "error",
            "message": "No tours found"
        }, status=404)

    serializer = ScheduledTourWithTourDataSerializer(nearest_tour)
    return JsonResponse({
        "status": "ok",
        "data": serializer.data,
        "message": None
    })


@api_view(['POST'])
def add_entry(request):
    try:
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                "status": "ok",
                "message": None
            })

        raise Exception("Can't serialize data")
    except Exception as err:
        return JsonResponse({
            "status": "error",
            "message": err
        })
