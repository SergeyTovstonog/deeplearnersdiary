# Generated by Django 4.1.5 on 2023-01-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPublications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('theme', models.CharField(max_length=150, verbose_name='Theme of publication')),
                ('anons', models.CharField(max_length=250, verbose_name='Anons')),
                ('full_text', models.TextField(verbose_name='Text')),
                ('date', models.DateField(verbose_name='Date of publication')),
            ],
        ),
    ]
