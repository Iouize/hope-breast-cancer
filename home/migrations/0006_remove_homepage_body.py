# Generated by Django 4.0.6 on 2022-07-18 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
    ]
