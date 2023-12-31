# Generated by Django 4.1.7 on 2023-04-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewindgroup', '0014_news_image_news_post_id_news_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('id',), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='clips',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='concert',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Город концерта'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='place',
            field=models.CharField(max_length=255, verbose_name='Место концерта'),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
    ]
