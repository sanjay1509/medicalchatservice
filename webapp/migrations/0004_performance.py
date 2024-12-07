# Generated by Django 3.1.3 on 2023-03-29 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_bookings_doctors'),
    ]

    operations = [
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alg_name', models.CharField(max_length=100)),
                ('sc1', models.FloatField()),
                ('sc2', models.FloatField()),
                ('sc3', models.FloatField()),
                ('sc4', models.FloatField()),
            ],
        ),
    ]
