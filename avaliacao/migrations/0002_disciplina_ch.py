# Generated by Django 3.2.8 on 2023-09-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='ch',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]