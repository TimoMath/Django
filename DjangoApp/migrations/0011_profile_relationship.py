# Generated by Django 4.1.5 on 2023-01-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0010_profile_firstname_profile_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='relationship',
            field=models.TextField(blank=True),
        ),
    ]
