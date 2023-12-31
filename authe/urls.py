from django.urls import path
from authe.views import register_view, login_view, logout_view

urlpatterns = [
    path(route='register/', view=register_view, name="register"),
    path(route='login/', view=login_view, name="login"),
    path(route='logout/', view=logout_view, name="logout"),
]