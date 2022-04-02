from ckeditor.fields import RichTextField
from django.db import models


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

    class Meta():
        verbose_name_plural = "Фото"
        verbose_name = "Фото"


class Static(models.Model):
    name = models.CharField(
        "Наименование шаблона",
        max_length=32,
        help_text="Название шаблона для поиска нужного шаблона в общем списке для данной страницы",
        blank=False,
    )
    status = models.BooleanField(
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
        abstract = True


class About(Static):
    class Meta():
        abstract = False
        verbose_name_plural = "О проекте"
        verbose_name = "О проекте"


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


class Update(models.Model):
    name = models.CharField(
        "Заголовок обновления",
        max_length=512,
        help_text="Короткое описание проделанной работы",
        blank=False,
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
        default='event/default.jpg'
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

    class Meta():
        verbose_name_plural = "Мероприятия"
        verbose_name = "Мероприятие"
        ordering = ['date']


class Archive(models.Model):
    # TODO: архив
    class Meta():
        verbose_name_plural = "Архив"
        verbose_name = "Архив"
