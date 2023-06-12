# Generated by Django 4.1.7 on 2023-06-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smart_emailApp", "0016_errorreport"),
    ]

    operations = [
        migrations.CreateModel(
            name="Assets",
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
                (
                    "image_asset",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="email_assets/images/",
                    ),
                ),
                ("asset_name", models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]