# Generated by Django 4.0.3 on 2022-04-06 13:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_update_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='html',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Страница мероприятия', verbose_name='Страница мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='Короткое описание обновления', max_length=2048, verbose_name='Описание'),
        ),
    ]
