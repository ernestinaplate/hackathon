# Generated by Django 2.2 on 2019-04-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagweb', '0004_auto_20190429_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_profesion', models.CharField(max_length=30)),
            ],
        ),
    ]
