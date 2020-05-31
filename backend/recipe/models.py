from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    recipeYield = models.CharField(max_length=20)
    isVegetarian = models.BooleanField()
    isVegan = models.BooleanField()
    prepTime = models.CharField(max_length=15)
    cookTime = models.CharField(max_length=15)
    cookingMethod = models.CharField(max_length=15)
    temp = models.IntegerField()
    description = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.name 
