# Generated by Django 3.2.8 on 2023-07-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
    ]
