# Generated by Django 3.2.9 on 2021-12-25 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_rename_imag_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='img',
            new_name='image',
        ),
    ]
