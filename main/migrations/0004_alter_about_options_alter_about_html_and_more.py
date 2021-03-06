# Generated by Django 4.0.3 on 2022-04-01 13:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_about_alter_contact_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О проекте', 'verbose_name_plural': 'О проекте'},
        ),
        migrations.AlterField(
            model_name='about',
            name='html',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Содержание страницы'),
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(help_text='Название шаблона для поиска нужного шаблона в общем списке для данной страницы', max_length=32, verbose_name='Наимнование шаблона'),
        ),
    ]
