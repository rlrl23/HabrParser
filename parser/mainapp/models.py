from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя автора", unique=True)
    link = models.CharField(
        max_length=200, verbose_name="Ссылка на страницу автора", unique=True
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name


class Hab(models.Model):
    name = models.CharField(max_length=200, verbose_name="Заголовок")
    link = models.CharField(
        unique=True, max_length=200, verbose_name="Ссылка на страницу хаба"
    )

    class Meta:
        verbose_name = "Хаб"
        verbose_name_plural = "Хабы"

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Дата создания")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    link = models.CharField(
        unique=True, max_length=200, verbose_name="Ссылка на страницу статьи"
    )
    text = models.TextField(verbose_name="Текст статьи")
    hab = models.ForeignKey(Hab, verbose_name="Хаб", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
