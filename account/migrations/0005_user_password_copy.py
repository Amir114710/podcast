# Generated by Django 4.2.3 on 2024-12-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_user_image_user_is_online"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password_copy",
            field=models.TextField(blank=True, null=True),
        ),
    ]
