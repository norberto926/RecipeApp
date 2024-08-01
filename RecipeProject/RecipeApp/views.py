from rest_framework import generics
from .models import Recipe, Ingredient, RecipeIngredient
from .serializers import RecipeDetailSerializer, RecipeListSerializer, RecipeIngredientSerializer, IngredientSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    parser_classes = [MultiPartParser, FormParser]
    
class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
    
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    parser_classes = [MultiPartParser, FormParser]
    

class RecipeIngredientCreate(generics.CreateAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class RecipeIngredientUpdate(generics.UpdateAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()
        
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        ingredients_data = request.data.get('recipe_ingredients', [])

        # Delete specific RecipeIngredients
        for ingredient_data in ingredients_data:
            ingredient_id = ingredient_data.get('ingredient_id')
            if ingredient_id:
                RecipeIngredient.objects.filter(recipe=instance, ingredient_id=ingredient_id).delete()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
class RecipeIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer