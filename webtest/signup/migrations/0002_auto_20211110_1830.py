# Generated by Django 2.1 on 2021-11-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ccountry',
            field=models.CharField(choices=[('KOR', 'Korea'), ('USA', 'United State Of America'), ('JPN', 'Japen')], max_length=5),
        ),
    ]
