from django.shortcuts import render
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class ListRecipe(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class DetailRecipe(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer