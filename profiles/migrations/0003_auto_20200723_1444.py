# Generated by Django 3.0 on 2020-07-23 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200721_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indivdualuserprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='indivdualuserprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='indivdualuserprofile',
            name='middle_name',
        ),
    ]
