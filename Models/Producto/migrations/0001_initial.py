# Generated by Django 4.1.6 on 2023-03-02 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('stock', models.IntegerField(max_length=5)),
                ('fecha_vencimiento', models.DateField()),
                ('fecha_entrada', models.DateField()),
            ],
        ),
    ]
