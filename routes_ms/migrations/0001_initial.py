# Generated by Django 4.0 on 2021-12-21 00:01

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavPlace',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('userId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('startLatitude', models.FloatField()),
                ('startLongitude', models.FloatField()),
                ('endLatitude', models.FloatField()),
                ('endLongitude', models.FloatField()),
                ('startAddress', models.CharField(max_length=200)),
                ('endAddress', models.CharField(max_length=200)),
                ('userId', models.IntegerField()),
            ],
        ),
    ]