# Generated by Django 3.1.6 on 2021-02-09 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210209_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='body',
        ),
    ]
