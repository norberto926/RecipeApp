from .views import RecipeList, RecipeDetail, IngredientList, IngredientDetail
from django.urls import path
from . import views


urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('ingredients/', views.IngredientList.as_view(), name = 'ingredient-list'),
    path('ingredients/<int:pk>/', views.IngredientList.as_view(), name = 'ingredient-detail')
]