# Generated by Django 4.1.4 on 2023-03-12 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0002_blog_slug_alter_blog_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="author",
            old_name="name",
            new_name="Authorname",
        ),
        migrations.RenameField(
            model_name="tags",
            old_name="name",
            new_name="tagname",
        ),
    ]
