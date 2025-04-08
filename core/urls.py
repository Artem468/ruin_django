from django.urls import path

from core import views

urlpatterns = [
    path("tours", views.get_tours, name="get_tours"),
    path("tours/<int:tour_id>", views.get_tour_by_id, name="get_tour_by_id"),
    path("points/<int:tour_id>", views.get_tour_points, name="get_tour_points"),
]