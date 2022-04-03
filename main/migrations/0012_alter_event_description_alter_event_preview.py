# Generated by Django 4.0.3 on 2022-04-02 10:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_event_rename_contact_team_alter_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='Подробное описание мероприятия', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='preview',
            field=models.ImageField(blank=True, default='event/default.jpg', help_text='Фото, которое будет отображаться в общем списке мероприятий', upload_to='event/', verbose_name='Превью мероприятия'),
        ),
    ]