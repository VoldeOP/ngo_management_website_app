# Generated by Django 3.2.4 on 2022-09-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('Mobile', models.CharField(max_length=12)),
                ('Message', models.TextField()),
            ],
        ),
    ]
