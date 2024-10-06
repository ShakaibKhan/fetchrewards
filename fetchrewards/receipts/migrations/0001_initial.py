# Generated by Django 4.2.16 on 2024-10-03 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('shortDescription', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('retailer', models.CharField(max_length=200)),
                ('purchaseDate', models.DateField()),
                ('purchaseTime', models.CharField(max_length=200)),
                ('items', models.ManyToManyField(to='receipts.item')),
            ],
        ),
    ]
