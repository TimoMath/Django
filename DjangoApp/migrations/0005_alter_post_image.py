# Generated by Django 4.1.5 on 2023-01-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0004_remove_profile_email_remove_profile_working_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='post_image.jpg', null=True, upload_to='post_image'),
        ),
    ]
