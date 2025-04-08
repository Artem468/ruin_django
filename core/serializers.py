from rest_framework import serializers

from core.models import Tour, Point, Entry, ScheduledTour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class ScheduledTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledTour
        fields = '__all__'


class ScheduledTourWithTourDataSerializer(serializers.ModelSerializer):
    tour = TourSerializer()

    class Meta:
        model = ScheduledTour
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
