# Generated by Django 2.1.2 on 2018-10-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mymodel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfield2', models.IntegerField()),
            ],
        ),
    ]
