# Generated by Django 2.2.7 on 2019-12-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20191203_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='fale',
            field=models.FileField(default=1, upload_to='game/static/script_my'),
            preserve_default=False,
        ),
    ]