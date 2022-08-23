# Generated by Django 4.1 on 2022-08-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Місто',
                'verbose_name_plural': 'Міста',
                'ordering': ['name'],
            },
        ),
    ]
