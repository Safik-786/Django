# Generated by Django 5.0 on 2023-12-22 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=70)),
                ('stuemail', models.CharField(max_length=70)),
                ('stuepass', models.CharField(max_length=70)),
            ],
        ),
    ]
