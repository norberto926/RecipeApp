from django.db import models
from users.models import NewUser

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=6)
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    
    @property
    def total_protein(self):
        return sum(ri.ingredient.protein * ri.quantity for ri in self.recipe_ingredients.all())/100

    @property
    def total_carbohydrates(self):
        return sum(ri.ingredient.carbohydrates * ri.quantity for ri in self.recipe_ingredients.all())/100

    @property
    def total_fat(self):
        return sum(ri.ingredient.fat * ri.quantity for ri in self.recipe_ingredients.all())/100

    @property
    def total_calories(self):
        return sum((ri.ingredient.protein * 4 + ri.ingredient.carbohydrates * 4 + ri.ingredient.fat * 9) * ri.quantity for ri in self.recipe_ingredients.all())/100

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=6)
    name = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe, through='RecipeIngredient')
    protein = models.IntegerField()
    carbohydrates = models.IntegerField()
    fat = models.IntegerField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    
    def calories(self):
        return (self.protein * 4) + (self.carbohydrates * 4) + (self.fat * 9)
    

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipe_ingredients', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name='ingredient_recipes', on_delete=models.CASCADE)
    quantity = models.IntegerField()
