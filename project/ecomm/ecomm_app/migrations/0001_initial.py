# Generated by Django 4.2.5 on 2023-10-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('price', models.FloatField()),
                ('pdetails', models.CharField(max_length=100, verbose_name='Product Details')),
                ('cat', models.IntegerField(verbose_name='Category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Avilable')),
            ],
        ),
    ]
