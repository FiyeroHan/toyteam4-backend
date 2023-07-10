# Generated by Django 4.2.3 on 2023-07-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone', '0008_video_recommended_video_delete_recommended_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='recommended_Video',
        ),
        migrations.AddField(
            model_name='video',
            name='recommended_Video',
            field=models.ManyToManyField(null=True, to='youtube_clone.video'),
        ),
    ]