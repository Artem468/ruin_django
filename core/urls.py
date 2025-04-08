from django.urls import path

from core import views

urlpatterns = [
    path("tours", views.get_tours, name="get_tours"),
    path("scheduledTours", views.get_scheduled_tours, name="get_scheduled_tours"),
    path("tours/<int:tour_id>", views.get_tour_by_id, name="get_tour_by_id"),
    path("tours/nearest", views.get_nearest_tour, name="get_nearest_tour"),
    path("points/<int:tour_id>", views.get_tour_points, name="get_tour_points"),
    path("entry/add", views.add_entry, name="add_entry"),
]