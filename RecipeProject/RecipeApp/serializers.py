from rest_framework import serializers
from .models import Recipe, Ingredient, RecipeIngredient


class IngredientSerializer(serializers.ModelSerializer):
    
    calories = serializers.ReadOnlyField()
    
    class Meta:
            model = Ingredient
            fields = ['id', 'name', 'protein', 'carbohydrates', 'fat', 'calories', 'photo', 'user']
            

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())


    class Meta:
        model = RecipeIngredient
        fields = ['id', 'recipe', 'ingredient', 'quantity']
        
        
class RecipeDetailSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    total_protein = serializers.ReadOnlyField()
    total_carbohydrates = serializers.ReadOnlyField()
    total_fat = serializers.ReadOnlyField()
    total_calories = serializers.ReadOnlyField()
    
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'recipe_ingredients', 'total_protein', 'total_carbohydrates', 'total_fat', 'total_calories', 'photo', 'user']
        
class RecipeListSerializer(serializers.ModelSerializer):
    total_protein = serializers.ReadOnlyField()
    total_carbohydrates = serializers.ReadOnlyField()
    total_fat = serializers.ReadOnlyField()
    total_calories = serializers.ReadOnlyField()
    
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'total_protein', 'total_carbohydrates', 'total_fat', 'total_calories', 'photo', 'user']
        
        
        
