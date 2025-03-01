from django.urls import path

from cinema.views import movie_list, movie_detail, CinemaHallViewSet, GenreList, GenreDetail, ActorList, ActorDetail

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("genre/", GenreList.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actor/", ActorList.as_view(), name="actor-list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahall/", cinema_hall_list, name="cinemahall-list"),
    path("cinemahall/<int:pk>/", cinema_hall_detail, name="cinemahall-detail")
]

app_name = "cinema"
