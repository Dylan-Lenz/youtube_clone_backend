# Generated by Django 4.1.2 on 2022-10-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='text',
            field=models.CharField(default=1, max_length=144),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='video_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
