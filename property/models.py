from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField('Новостройка', blank=True, null=True)
    likes = models.ManyToManyField(
        User,
        verbose_name='Кто лайкнул',
        related_name='flat_likes',
    )

    def __str__(self) -> str:
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    flat = models.ForeignKey(
        Flat,
        verbose_name='Квартира, на которую жаловались',
        on_delete=models.CASCADE,
        related_name='complaints'
    )
    user = models.ForeignKey(
        User,
        verbose_name='Кто жаловался',
        on_delete=models.CASCADE,
        related_name='complaints'
    )
    text = models.TextField(
        'Текст жалобы',
        blank=True,
        null=False
    )

    def __str__(self) -> str:
        return f'<{self.user.username}> {self.flat.address}'


class Owner(models.Model):
    full_name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phone = models.CharField('Номер владельца', max_length=20)
    formatted_phone = PhoneNumberField(
        'Нормализованный номер владельца',
        region='RU',
        blank=True,
        null=True
    )
    flats = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности',
        related_name='owners',
    )

    def __str__(self) -> str:
        return f'<{self.full_name}> {self.formatted_phone}'
