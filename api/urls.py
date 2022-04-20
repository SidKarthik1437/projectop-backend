from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("probs/", views.getProbs, name="probs"),
    path("probs/create", views.createProb, name="create-script"),
    path("probs/<str:pk>/update/", views.updateProb, name="update-script"),
    path("probs/<str:pk>/delete/", views.deleteProb, name="delete-script"),
    path("probs/<str:pk>/", views.getProb, name="prob"),

]
