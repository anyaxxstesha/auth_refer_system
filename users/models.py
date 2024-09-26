from django.contrib.auth.models import AbstractUser
from django.db import models

NULL = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=32, unique=True, verbose_name='Номер телефона',
                             help_text='Укажите номер телефона')
    invite_code = models.CharField(max_length=6, verbose_name='Инвайт-код', help_text='Генерируется при регистрации')
    invited_by = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='referrals',
                                   verbose_name='Кем приглашён', help_text='Пользователь, который Вас пригласил',
                                   **NULL)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone
