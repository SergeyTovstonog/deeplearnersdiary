# Generated by Django 4.1.5 on 2023-01-26 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpublications',
            options={'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
    ]
