# Generated by Django 3.2.13 on 2022-05-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=3)),
                ('source', models.TextField()),
                ('purchaseDate', models.DateField()),
                ('purchaseCost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]