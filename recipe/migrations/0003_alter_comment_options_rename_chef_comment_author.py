# Generated by Django 4.2.11 on 2024-04-14 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_options_alter_recipe_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='chef',
            new_name='author',
        ),
    ]
