# Generated by Django 4.0.6 on 2022-07-22 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('blog', '0010_alter_blogpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='banner_background_image',
            field=models.ForeignKey(help_text='Image de la banière', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='button',
            field=models.ForeignKey(blank=True, help_text='Lien optionnel', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='button_text',
            field=models.CharField(default='En savoir plus', help_text='Texte du Bouton', max_length=50),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='lead_text',
            field=models.CharField(blank=True, help_text='Sous-titre', max_length=140),
        ),
    ]