# Generated by Django 3.1 on 2020-10-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthreport',
            name='present_weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='healthreport',
            name='weight_at_birth',
            field=models.IntegerField(default=0),
        ),
    ]