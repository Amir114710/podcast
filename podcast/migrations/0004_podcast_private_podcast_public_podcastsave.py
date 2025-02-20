# Generated by Django 4.2.3 on 2024-11-30 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("podcast", "0003_alter_podcast_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="podcast",
            name="private",
            field=models.BooleanField(default=False, verbose_name="خصوصی"),
        ),
        migrations.AddField(
            model_name="podcast",
            name="public",
            field=models.BooleanField(default=False, verbose_name="منتشر شده"),
        ),
        migrations.CreateModel(
            name="PodcastSave",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "podcast",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="podcast_saves",
                        to="podcast.podcast",
                        verbose_name="پادکست",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="podcast_saves",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "ذخیره  برای پادسکت",
                "verbose_name_plural": "ذخیره ها برای پادکست",
                "ordering": ("-created",),
            },
        ),
    ]
