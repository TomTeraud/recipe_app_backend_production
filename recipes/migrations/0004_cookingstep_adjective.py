# Generated by Django 4.2.7 on 2023-12-16 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_adjetive_adjective'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookingstep',
            name='adjective',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.adjective'),
        ),
    ]
