# Generated by Django 2.1.2 on 2018-10-18 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]