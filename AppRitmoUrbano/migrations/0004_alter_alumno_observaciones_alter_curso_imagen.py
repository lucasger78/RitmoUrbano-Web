# Generated by Django 4.0.3 on 2022-06-07 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRitmoUrbano', '0003_alter_alumno_imagen_alter_profesor_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='observaciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/cursos'),
        ),
    ]