# Generated by Django 4.2.7 on 2023-12-12 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_info', '0003_alter_recipeingredient_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='type_shoping_only',
            new_name='type_shoping_valid',
        ),
    ]
