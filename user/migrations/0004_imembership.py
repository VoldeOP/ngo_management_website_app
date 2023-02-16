# Generated by Django 3.2.4 on 2022-09-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_iblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='imembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.TextField()),
                ('mcode', models.IntegerField(max_length=10)),
                ('mcity', models.CharField(max_length=50)),
                ('memail', models.CharField(max_length=50)),
                ('mbank', models.IntegerField(max_length=15)),
                ('mcompany', models.CharField(max_length=100)),
                ('madd', models.CharField(max_length=200)),
            ],
        ),
    ]