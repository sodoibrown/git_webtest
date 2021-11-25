# Generated by Django 2.1 on 2021-11-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20, verbose_name='cname')),
                ('cemail', models.EmailField(max_length=120, verbose_name='cemail')),
                ('ccountry', models.CharField(choices=[('KOR', 'Korea'), ('USA', 'UnitedStateOfAmerica'), ('JPN', 'Japen')], max_length=5)),
            ],
        ),
    ]