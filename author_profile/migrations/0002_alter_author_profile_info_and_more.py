# Generated by Django 4.1.4 on 2023-03-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("author_profile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author_profile",
            name="info",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="author_profile",
            name="instagram",
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="author_profile",
            name="linkedin",
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="author_profile",
            name="twitter",
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="author_profile",
            name="username",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="author_profile",
            name="youtube",
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]