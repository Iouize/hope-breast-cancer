# Generated by Django 4.0.6 on 2022-07-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_menuitem_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='icon_fontawesome',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]