# Generated by Django 5.0.1 on 2024-02-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='account/static/images_root/user_profil/default_image.png', upload_to='account/static/images_root/user_profil/'),
        ),
    ]
