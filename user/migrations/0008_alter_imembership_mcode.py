# Generated by Django 3.2.4 on 2022-09-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20220905_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imembership',
            name='mcode',
            field=models.IntegerField(),
        ),
    ]
