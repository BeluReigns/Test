# Generated by Django 5.0.2 on 2024-03-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calzado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('talla', models.CharField(max_length=10)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Miscelaneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
                ('talla', models.CharField(max_length=10)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenda', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('talla', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
