# Generated by Django 5.0.1 on 2024-02-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_alter_videos_logo_delete_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos_root',
            name='logo',
            field=models.ImageField(default='videos_root/static/medias/logo/default_logo.png', upload_to='videos_root/static/medias/logo/'),
        ),

    ]