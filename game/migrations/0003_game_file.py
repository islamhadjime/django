# Generated by Django 2.2.7 on 2019-12-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20191202_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]