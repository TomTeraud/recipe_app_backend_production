# Generated by Django 4.2.7 on 2023-11-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_recipe_servings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=1),
        ),
    ]
