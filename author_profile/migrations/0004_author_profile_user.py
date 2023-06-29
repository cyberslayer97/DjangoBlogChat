# Generated by Django 4.1.4 on 2023-03-16 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("author_profile", "0003_rename_profile_tags_author_profile_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="author_profile",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
