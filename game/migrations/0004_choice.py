# Generated by Django 4.0.4 on 2022-06-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game_vote_1_game_vote_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('voted_num', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
