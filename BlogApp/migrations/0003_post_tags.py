# Generated by Django 5.1.2 on 2024-11-11 12:17

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_alter_post_status_alter_post_title_comment'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
