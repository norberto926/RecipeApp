from rest_framework import serializers
from .models import Recipe, Ingredient, RecipeIngredient

class IngredientSerializer(serializers.ModelSerializer):
    
    calories = serializers.ReadOnlyField()
    
    class Meta:
            model = Ingredient
            fields = ['id', 'name', 'protein', 'carbohydrates', 'fat', 'calories']
            

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']
        
        
class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True, read_only=True)
    total_protein = serializers.ReadOnlyField()
    total_carbohydrates = serializers.ReadOnlyField()
    total_fat = serializers.ReadOnlyField()
    total_calories = serializers.ReadOnlyField()
    
    class Meta:
        model = Recipefields = ['id', 'name', 'description', 'ingredients', 'total_protein', 'total_carbohydrates', 'total_fat', 'total_calories']
        
        
        
