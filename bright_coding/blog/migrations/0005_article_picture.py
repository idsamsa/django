# Generated by Django 4.0 on 2022-01-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(default='article.png', null=True, upload_to='articles/'),
        ),
    ]