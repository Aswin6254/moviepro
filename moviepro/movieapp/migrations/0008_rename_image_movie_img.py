# Generated by Django 3.2.9 on 2021-12-27 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0007_alter_movie_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='image',
            new_name='img',
        ),
    ]
