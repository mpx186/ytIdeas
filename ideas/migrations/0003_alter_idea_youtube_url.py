# Generated by Django 4.0.6 on 2022-07-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_alter_idea_youtube_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='youtube_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
