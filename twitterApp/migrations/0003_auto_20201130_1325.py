# Generated by Django 3.1.3 on 2020-11-30 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterApp', '0002_tweet_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='username',
            new_name='author',
        ),
    ]
