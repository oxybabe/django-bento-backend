# Generated by Django 4.2.2 on 2023-06-22 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0004_alter_appetizer_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appetizer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='dessert',
            name='price',
        ),
        migrations.RemoveField(
            model_name='maincourse',
            name='price',
        ),
    ]
