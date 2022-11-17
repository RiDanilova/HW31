from django.core.validators import MinLengthValidator
from django.db import models

from users.models import User


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    name = models.CharField(verbose_name="Название категории", max_length=100, unique=True)
    slug = models.CharField(verbose_name="Поле 'slug'", validators=[MinLengthValidator(5)], max_length=10, unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    name = models.CharField(verbose_name="Название объявления", validators=[MinLengthValidator(10)], max_length=100, unique=True)
    author = models.ForeignKey(User, verbose_name="Автор", null=True, on_delete=models.CASCADE, related_name="ads")
    price = models.PositiveIntegerField(verbose_name="Цена", null=True)
    description = models.CharField(verbose_name="Подробная информация", max_length=500, null=True, blank=True)  # blank - для Django-админки
    is_published = models.BooleanField(verbose_name="Размещено ли объявление?", help_text="Если данный пункт отмечен - объявление размещено", default=False)
    image = models.ImageField(verbose_name="Изображение", upload_to="images",  null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория", null=True, on_delete=models.CASCADE, related_name="ads")

    def __str__(self):
        return self.name


class Selection(models.Model):
    class Meta:
        verbose_name = "Подборка объявлений"
        verbose_name_plural = "Подборки объявлений"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="selections")
    name = models.CharField(max_length=100, unique=True)
    items = models.ManyToManyField(Ad)

    def __str__(self):
        return self.name
