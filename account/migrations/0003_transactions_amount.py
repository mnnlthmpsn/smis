# Generated by Django 3.1 on 2020-10-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201004_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]