# Generated by Django 2.1.3 on 2018-12-04 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='creation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='disposal_date',
            field=models.DateField(),
        ),
    ]
