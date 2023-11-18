from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Модель')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость')
    image = models.URLField(verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, verbose_name='URL')

    def save(self, *args, **kwargs):       # Эта функция не работает
        if not self.id:
            self.slug = slugify(self.name)

        super(Phone, self).save(*args, **kwargs)
