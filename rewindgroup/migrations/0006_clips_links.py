# Generated by Django 4.1.4 on 2023-03-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewindgroup', '0005_remove_concert_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='clips_img/%Y/%m/%d', verbose_name='Превью')),
                ('link', models.CharField(max_length=300, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(max_length=100, verbose_name='Ресурс')),
                ('link', models.CharField(max_length=300, verbose_name='Ссылка')),
            ],
        ),
    ]