# Generated by Django 4.2.6 on 2023-11-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zlash_news_api', '0005_alter_newsmodel_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsmodel',
            name='published_at',
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='description',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
