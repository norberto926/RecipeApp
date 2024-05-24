from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe, through='RecipeIngredient')
    protein = models.IntegerField()
    carbohydrates = models.IntegerField()
    fat = models.IntegerField()
    
    def calories(self):
        return (self.protein * 4) + (self.carbohydrates * 4) + (self.fat * 9)
    

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    @property
    def total_protein(self):
        return sum(ingredient.protein * ri.quantity for ri in self.recipeingredient_set.all())

    @property
    def total_carbohydrates(self):
        return sum(ingredient.carbohydrates * ri.quantity for ri in self.recipeingredient_set.all())

    @property
    def total_fat(self):
        return sum(ingredient.fat * ri.quantity for ri in self.recipeingredient_set.all())

    @property
    def total_calories(self):
        return sum((ingredient.protein * 4 + ingredient.carbohydrates * 4 + ingredient.fat * 9) * ri.quantity for ri in self.recipeingredient_set.all())

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)
