# Generated by Django 4.2.7 on 2023-11-28 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zlash_news_api', '0002_alter_newsmodel_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('content', models.TextField()),
                ('photo', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 20, 6, 48, 730744, tzinfo=datetime.timezone.utc)),
        ),
    ]