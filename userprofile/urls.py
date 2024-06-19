from django.urls import path
from . import views


urlpatterns = [
    path("profile", views.get_profile, name="profile"),
    path("profile/update", views.edit_profile, name="edit_profile"),
    path("profile/change-password", views.change_password, name="change_password"),
]
