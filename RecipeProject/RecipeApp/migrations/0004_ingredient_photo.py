# Generated by Django 5.0.6 on 2024-07-31 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeApp', '0003_recipe_photo_alter_recipeingredient_ingredient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]