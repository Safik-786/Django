# Generated by Django 5.0 on 2024-06-12 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contractor',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
