# Generated by Django 3.1.1 on 2020-11-14 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_post_posttag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='PostTag',
        ),
    ]