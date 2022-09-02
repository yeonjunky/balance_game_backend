# Generated by Django 4.0.4 on 2022-08-02 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0020_alter_vote_choice_alter_vote_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
