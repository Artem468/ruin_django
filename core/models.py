from django.db import models


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return str(self.id)


class Tour(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    place = models.CharField(
        verbose_name="Место начала",
        max_length=255
    )
    price = models.FloatField(
        verbose_name="Цена",
    )
    max_members = models.IntegerField(
        verbose_name="Максимум участников",
    )
    image = models.ImageField(
        verbose_name="Картинка",
        upload_to='images/',
        max_length=255
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
        db_table = "tours"


class ScheduledTour(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Тур")
    start_at = models.DateTimeField(verbose_name="Начало")
    end_at = models.DateTimeField(verbose_name="Конец")
    guide = models.CharField(max_length=255, verbose_name="Гид")

    def __str__(self):
        return f"{self.tour.name}"

    class Meta:
        verbose_name = "Запланированный тур"
        verbose_name_plural = "Запланированные туры"
        db_table = "scheduled_tours"


class Point(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Тур")
    number = models.IntegerField(verbose_name="Номер точки")
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(max_length=255, verbose_name="Картинка", upload_to='images/')

    def __str__(self):
        return f"{self.number}. {self.name}"

    class Meta:
        verbose_name = "Точка остановки"
        verbose_name_plural = "Точки остановки"
        db_table = "points"


class Entry(models.Model):
    scheduled_tour = models.ForeignKey(ScheduledTour, on_delete=models.CASCADE, verbose_name="Запланированный тур")
    telegram_id = models.BigIntegerField(verbose_name="Telegram ID", null=True, default=None)
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Почта", null=True, default=None)
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    is_need_lunch = models.BooleanField(verbose_name="Обед")
    is_need_notify = models.BooleanField(verbose_name="Уведомление")
    count_members = models.IntegerField(verbose_name="Количество человек")
    comment = models.TextField(null=True, blank=True, default=None, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.name} — {self.scheduled_tour}"

    class Meta:
        verbose_name = "Запись на тур"
        verbose_name_plural = "Записи на тур"
        db_table = "entries"
