# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0027_auto_20170629_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=50)),
                ('user_email', models.EmailField(blank=True, max_length=100)),
                ('user_url', models.URLField(blank=True)),
                ('content', models.TextField(verbose_name='评论')),
                ('submit_date', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='easy_comment.Comment', verbose_name='父级评论')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='文章')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]