# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 08:41
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy_comment', '0002_auto_20170702_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_url',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='评论'),
        ),
    ]