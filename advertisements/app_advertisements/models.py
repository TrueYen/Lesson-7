from django.db import models


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг?', help_text='Отметьте, если торг уместен?')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


def __str__(self):
    return f'Advertisements(id={self.id}, title={self.title}, price={self.price})'


class Meta:
    db_table = 'advertisements'
