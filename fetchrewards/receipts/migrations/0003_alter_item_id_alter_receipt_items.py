# Generated by Django 4.2.16 on 2024-10-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_remove_receipt_items_receipt_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='items',
            field=models.JSONField(),
        ),
    ]
