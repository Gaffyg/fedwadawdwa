# Generated by Django 4.1.7 on 2023-04-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewindgroup', '0016_alter_clips_image_alter_clips_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='resourse',
        ),
        migrations.AddField(
            model_name='links',
            name='platform',
            field=models.CharField(default=1, max_length=255, verbose_name='Платформа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.URLField(verbose_name='Ссылка'),
        ),
    ]