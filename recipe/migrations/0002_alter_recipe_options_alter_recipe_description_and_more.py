# Generated by Django 4.2.11 on 2024-04-12 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-posted_on']},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dish_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Curries', 'Curries'), ('Snacks', 'Snacks'), ('Drinks', 'Drinks')], default='breakfast', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.CharField(choices=[('5 minutes', '5 min'), ('10 minutes', '10 min'), ('15 minutes', '15 min'), ('20 minutes', '20 min'), ('30 minutes', '30 min'), ('45 minutes', '45 min'), ('1 hour', '1 hour'), ('1+ hour', 'More than 1h')], default='15 minutes', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipe.recipe')),
            ],
        ),
    ]