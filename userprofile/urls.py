from django.urls import path
from . import views


urlpatterns = [
    path("profile", views.get_profile, name="profile"),
    path("profile/update", views.edit_profile, name="edit_profile"),
]
