# Generated by Django 4.2.7 on 2023-12-16 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_description_name_lv_description_name_rus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookingstep',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='cookingstep',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.unit'),
        ),
    ]
