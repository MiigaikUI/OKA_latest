from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
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
        default='contact/default.jpg'
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

    class Meta():
        verbose_name_plural = "Команда"
        verbose_name = "Участника"


class Image(models.Model):
    name = models.CharField(
        "Наимнование шаблона",
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

    class Meta():
        verbose_name_plural = "Фото"
        verbose_name = "Фото"


class About(models.Model):
    name = models.CharField(
        "Наимнование шаблона",
        max_length=32,
        help_text="Название шаблона для поиска нужного шаблона в общем списке для данной страницы",
        blank=False,
    )
    status = models.BooleanField(
        "Статус",
        help_text="Статус указывет на шаблон который будет отображено на странице",
    )
    html = RichTextField(
        "Содержание страницы",
        blank=True,
    )

    @classmethod
    def get_current(cls):
        result = cls.objects.all().filter(status=1)
        return result.first().html

    def save(self, *args, **kwargs):
        if self.status:
            try:
                temp = self.__class__.objects.get(status=True)
                if self != temp:
                    temp.status = False
                    temp.save()
            except self.__class__.DoesNotExist:
                pass
        super(self.__class__, self).save(*args, **kwargs)

    class Meta():
        verbose_name_plural = "О проекте"
        verbose_name = "О проекте"


class Region(models.Model):
    name = models.CharField(
        "Наимнование шаблона",
        max_length=32,
        help_text="Название шаблона для поиска нужного шаблона в общем списке для данной страницы",
        blank=False,
    )
    status = models.BooleanField(
        "Статус",
        help_text="Статус указывет на шаблон который будет отображено на странице",
    )
    html = RichTextField(
        "Содержание страницы",
        blank=True,
    )

    @classmethod
    def get_current(cls):
        result = cls.objects.all().filter(status=1)
        return result.first().html

    def save(self, *args, **kwargs):
        if self.status:
            try:
                temp = self.__class__.objects.get(status=True)
                if self != temp:
                    temp.status = False
                    temp.save()
            except self.__class__.DoesNotExist:
                pass
        super(self.__class__, self).save(*args, **kwargs)

    class Meta():
        verbose_name_plural = "О регионе"
        verbose_name = "О регионе"


class Results(models.Model):
    name = models.CharField(
        "Наимнование шаблона",
        max_length=32,
        help_text="Название шаблона для поиска нужного шаблона в общем списке для данной страницы",
        blank=False,
    )
    status = models.BooleanField(
        "Статус",
        help_text="Статус указывет на шаблон который будет отображено на странице",
    )
    html = RichTextField(
        "Содержание страницы",
        blank=True,
    )

    @classmethod
    def get_current(cls):
        result = cls.objects.all().filter(status=1)
        return result.first().html

    def save(self, *args, **kwargs):
        if self.status:
            try:
                temp = self.__class__.objects.get(status=True)
                if self != temp:
                    temp.status = False
                    temp.save()
            except self.__class__.DoesNotExist:
                pass
        super(self.__class__ , self).save(*args, **kwargs)

    class Meta():
        verbose_name_plural = "Результаты"
        verbose_name = "Результат"


""" 
обновления,
мероприятия (
    списочная страница (
        дата и название мероприятия, анонс
    ) 
    и каждая новость в 	отдельной странице, с фотографиями
),
архив
"""
