# Generated by Django 2.1 on 2021-11-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('fwork', models.CharField(max_length=150)),
                ('fdollar', models.IntegerField(default=0)),
                ('fsuccess', models.IntegerField(default=0)),
                ('fjob', models.IntegerField(default=0)),
                ('fcountry', models.CharField(max_length=50)),
                ('fability1', models.CharField(max_length=50)),
                ('fability2', models.CharField(max_length=50)),
                ('fability3', models.CharField(max_length=50)),
                ('fability4', models.CharField(max_length=50)),
            ],
        ),
    ]
