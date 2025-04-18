from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.UserList.as_view(), name="index"),
    path("users/<int:user_id>/", views.UserDetail.as_view(), name="detail"),
]
