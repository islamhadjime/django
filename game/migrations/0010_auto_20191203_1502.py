# Generated by Django 2.2.7 on 2019-12-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20191203_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='fale',
            field=models.FileField(upload_to='game/static/games_my'),
        ),
    ]