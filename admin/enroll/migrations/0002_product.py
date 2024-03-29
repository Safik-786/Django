# Generated by Django 5.0 on 2024-01-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodid', models.IntegerField()),
                ('prodname', models.CharField(max_length=50)),
                ('prodprice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('prodimage', models.ImageField(upload_to='')),
            ],
        ),
    ]
