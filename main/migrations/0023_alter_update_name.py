# Generated by Django 4.0.3 on 2022-04-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_team_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='name',
            field=models.CharField(blank=True, help_text='Короткое описание проделанной работы', max_length=512, verbose_name='Заголовок обновления'),
        ),
    ]
