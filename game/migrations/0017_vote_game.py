# Generated by Django 4.0.4 on 2022-07-03 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_remove_vote_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='game',
            field=models.ForeignKey(default=25, on_delete=django.db.models.deletion.CASCADE, to='game.game'),
            preserve_default=False,
        ),
    ]
