# Generated by Django 4.0.4 on 2022-06-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='title',
            field=models.CharField(default='foo', max_length=256),
            preserve_default=False,
        ),
    ]
