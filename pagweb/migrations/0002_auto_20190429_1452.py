# Generated by Django 2.2 on 2019-04-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancer',
            name='telefono1',
        ),
        migrations.AddField(
            model_name='freelancer',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='domicilio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='exp_previa',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='foto_de_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='profesion',
            field=models.CharField(choices=[('Fotografo', 'Fotografo'), ('Programador', 'Programador'), ('Profesor particular', 'Profesor particular')], max_length=30),
        ),
    ]
