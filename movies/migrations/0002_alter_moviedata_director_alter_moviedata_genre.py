# Generated by Django 5.0.3 on 2024-03-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='director',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(blank=True, default='Action', max_length=20),
        ),
    ]