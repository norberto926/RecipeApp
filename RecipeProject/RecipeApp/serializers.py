from rest_framework import serializers
from .models import Recipe, Ingredient, RecipeIngredient

class IngredientSerializer(serializers.ModelSerializer):
    
    calories = serializers.ReadOnlyField()
    
    class Meta:
            model = Ingredient
            fields = ['id', 'name', 'protein', 'carbohydrates', 'fat', 'calories']
            

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
    queryset=Ingredient.objects.all(), source='ingredient', write_only=True)
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:
        model = RecipeIngredient
        fields = ['id', 'recipe', 'ingredient', 'ingredient_id', 'quantity']
        
        
class RecipeDetailSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    total_protein = serializers.ReadOnlyField()
    total_carbohydrates = serializers.ReadOnlyField()
    total_fat = serializers.ReadOnlyField()
    total_calories = serializers.ReadOnlyField()
    
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'recipe_ingredients', 'total_protein', 'total_carbohydrates', 'total_fat', 'total_calories']
        
class RecipeListSerializer(serializers.ModelSerializer):
    total_protein = serializers.ReadOnlyField()
    total_carbohydrates = serializers.ReadOnlyField()
    total_fat = serializers.ReadOnlyField()
    total_calories = serializers.ReadOnlyField()
    
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'total_protein', 'total_carbohydrates', 'total_fat', 'total_calories']
        
        
        
