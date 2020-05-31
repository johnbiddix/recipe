from django.urls import path
from .views import ListRecipe, DetailRecipe

urlpatterns = [
    path('<int:pk>/', DetailRecipe.as_view()),
    path('', ListRecipe.as_view()),
]