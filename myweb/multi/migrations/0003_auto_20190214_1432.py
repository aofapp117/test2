# Generated by Django 2.1.4 on 2019-02-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi', '0002_auto_20190214_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
