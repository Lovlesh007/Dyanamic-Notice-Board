# Generated by Django 2.1.2 on 2018-10-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_mymodel2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel2',
            name='myfield2',
            field=models.CharField(max_length=35),
        ),
    ]
