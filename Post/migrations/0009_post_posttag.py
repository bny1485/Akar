# Generated by Django 3.1.1 on 2020-11-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0005_remove_tag_post'),
        ('Post', '0008_remove_post_posttag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='PostTag',
            field=models.ManyToManyField(blank=True, null=True, to='tag.Tag'),
        ),
    ]
