# Generated by Django 3.0 on 2020-07-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200729_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='modified',
            field=models.DateField(auto_now=True),
        ),
    ]
