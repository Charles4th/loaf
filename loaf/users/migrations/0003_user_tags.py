# Generated by Django 2.0.7 on 2018-07-20 06:38

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('users', '0002_auto_20180709_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
