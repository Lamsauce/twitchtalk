# Generated by Django 3.1.6 on 2021-02-11 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210209_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.game'),
            preserve_default=False,
        ),
    ]
