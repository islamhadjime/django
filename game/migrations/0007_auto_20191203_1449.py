# Generated by Django 2.2.7 on 2019-12-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20191203_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='fale',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]