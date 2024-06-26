# Generated by Django 4.2.11 on 2024-04-10 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("recipe_id", models.IntegerField()),
                ("title", models.CharField(max_length=200, unique=True)),
                ("description", models.SlugField(max_length=200, unique=True)),
                ("ingredients", models.TextField()),
                ("method", models.TextField()),
                ("dish_type", models.CharField(max_length=200)),
                ("prep_time", models.CharField(max_length=200)),
                ("posted_on", models.DateTimeField(auto_now_add=True)),
                (
                    "chef",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="kitchen_recipes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
