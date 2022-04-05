# Generated by Django 4.0.3 on 2022-04-04 17:45

import ckeditor.fields
from django.db import migrations, models
import main.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_about_status_alter_archive_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название шаблона для поиска нужного шаблона в общем списке для данной страницы', max_length=32, verbose_name='Наименование шаблона')),
                ('status', main.fields.UniqueBooleanField(help_text='Статус указывает на шаблон который будет отображено на странице', verbose_name='Статус')),
                ('html', ckeditor.fields.RichTextField(blank=True, verbose_name='Содержание страницы')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'abstract': False,
            },
        ),
    ]
