# Generated by Django 4.0.3 on 2022-04-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='description',
            field=models.TextField(help_text='Подробное описание обновления', max_length=2048, verbose_name='Описание'),
        ),
    ]
