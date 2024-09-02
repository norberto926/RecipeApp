from .views import RecipeList, RecipeDetail, IngredientList, IngredientDetail, RecipeIngredientCreate, RecipeIngredientDetail
from django.urls import path, include
from . import views


urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('ingredients/', views.IngredientList.as_view(), name = 'ingredient-list'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name = 'ingredient-detail'),
    path('recipe-ingredients/', RecipeIngredientCreate.as_view(), name='recipe-ingredient-create'),
    path('recipe-ingredients/<int:pk>/', RecipeIngredientDetail.as_view(), name='recipe-ingredient-detail'),
    path('user/', include('users.urls', namespace='users'))

]