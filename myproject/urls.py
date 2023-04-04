from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("world", views.world, name="world"),
    path("Sugyan", views.sugyan, name="Sugyan")
]
