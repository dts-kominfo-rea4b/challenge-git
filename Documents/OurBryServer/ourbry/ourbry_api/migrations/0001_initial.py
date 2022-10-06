# Generated by Django 4.0.3 on 2022-04-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMember',
            fields=[
                ('nis', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('status', models.CharField(max_length=20)),
                ('first_fmd', models.BinaryField(max_length=4000)),
                ('second_fmd', models.BinaryField(max_length=4000)),
            ],
        ),
    ]
