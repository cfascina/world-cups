# Generated by Django 4.0.4 on 2022-05-16 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('championships', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='championship',
            old_name='total_contries',
            new_name='total_countries',
        ),
    ]
