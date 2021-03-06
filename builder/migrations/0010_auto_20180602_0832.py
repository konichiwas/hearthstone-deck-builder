# Generated by Django 2.0.5 on 2018-06-02 08:32

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0009_auto_20180529_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='', upload_to='news-images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='new',
            name='title',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
