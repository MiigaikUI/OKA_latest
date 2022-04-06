import os

from ckeditor.fields import RichTextField
from django.db import models

from OKA import settings
from main.fields import UniqueBooleanField


class Static(models.Model):
    name = models.CharField(
        "Наименование шаблона",
        max_length=32,
        help_text="Название шаблона для поиска нужного шаблона в общем списке для данной страницы",
        blank=False,
    )
    status = UniqueBooleanField(
        "Статус",
        help_text="Статус указывает на шаблон который будет отображено на странице",
    )
    html = RichTextField(
        "Содержание страницы",
        blank=True,
    )

    @classmethod
    def get_current(cls):
        result = cls.objects.all().filter(status=1)
        return result.first().html

    class Meta():
        abstract = True


class About(Static):
    class Meta():
        abstract = False
        verbose_name_plural = "О проекте"
        verbose_name = "О проекте"


class Contact(Static):
    class Meta():
        abstract = False
        verbose_name_plural = "Контакты"
        verbose_name = "Контакт"


class Region(Static):
    class Meta():
        abstract = False
        verbose_name_plural = "О регионе"
        verbose_name = "О регионе"


class Results(Static):
    class Meta():
        abstract = False
        verbose_name_plural = "Результаты"
        verbose_name = "Результат"


class Archive(Static):
    # TODO: refactor to non-static page
    class Meta():
        abstract = False
        verbose_name_plural = "Архивы"
        verbose_name = "Архив"


class Team(models.Model):
    first_name = models.CharField(
        "Имя",
        max_length=32,
        help_text="Имя участника",
        blank=True,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=32,
        help_text="Фамилия участника",
        blank=True,
    )
    img = models.ImageField(
        "Фото",
        upload_to="contact/",
        help_text="Фото участника",
        blank=True,
        default='contact/default.png'
    )
    role = models.TextField(
        "Роль",
        max_length=4096,
        help_text="Роль участника в проекте",
        blank=True,
    )
    description = models.TextField(
        "Описание",
        max_length=256,
        help_text="Описание участника",
        blank=True,
    )


    def delete(self, *args, **kwargs):
        if self.img.name != "contact/default.png":
            os.remove(os.path.join(settings.MEDIA_ROOT, self.img.name))
        super().delete(*args, **kwargs)

    class Meta():
        ordering = ['id']
        verbose_name_plural = "Команда проекта"
        verbose_name = "Участника"


class Update(models.Model):
    name = models.CharField(
        "Заголовок обновления",
        max_length=512,
        help_text="Короткое описание проделанной работы",
        blank=True,
    )
    description = models.TextField(
        "Описание",
        max_length=2048,
        help_text="Подробное описание обновления",
        blank=False,
    )
    date = models.DateField(
        "Дата обновления",
        help_text="Дата, когда было сделано обновление",
        editable=True,
    )

    class Meta():
        verbose_name_plural = "Обновления"
        verbose_name = "Обновление"
        ordering = ['date']


class Event(models.Model):
    name = models.CharField(
        "Наименование мероприятия",
        max_length=512,
        help_text="Название мероприятия, которое будет отображаться в общем списке мероприятий",
        blank=False,
    )
    img = models.ImageField(
        "Превью мероприятия",
        upload_to="event/",
        help_text="Фото, которое будет отображаться в общем списке мероприятий",
        blank=True,
    )

    description = RichTextField(
        "Описание",
        help_text="Подробное описание мероприятия",
        blank=False,
    )
    date = models.DateField(
        "Дата проведения",
        help_text="Дата проведения мероприятия",
        editable=True,
    )

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.img.name))
        super().delete(*args, **kwargs)

    class Meta():
        verbose_name_plural = "Мероприятия"
        verbose_name = "Мероприятие"
        ordering = ['date']


class Image(models.Model):
    name = models.CharField(
        "Наименование шаблона",
        max_length=32,
        help_text="Название шаблона для поиска нужного шаблона в общем списке для данной страницы",
        blank=False,
    )
    img = models.ImageField(
        "Фото",
        upload_to="uploads/",
        help_text="Фото",
        blank=False,
    )

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.img.name))
        super().delete(*args, **kwargs)

    class Meta():
        verbose_name_plural = "Фото"
        verbose_name = "Фото"
