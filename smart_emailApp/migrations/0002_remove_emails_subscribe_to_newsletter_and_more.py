# Generated by Django 4.1.7 on 2023-03-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_emailApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emails',
            name='subscribe_to_newsletter',
        ),
        migrations.AlterField(
            model_name='emails',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]