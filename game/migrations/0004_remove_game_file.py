# Generated by Django 2.2.7 on 2019-12-02 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='file',
        ),
    ]