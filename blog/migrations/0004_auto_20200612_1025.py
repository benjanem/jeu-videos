# Generated by Django 2.2.13 on 2020-06-12 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
