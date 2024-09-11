# Generated by Django 4.2.3 on 2024-09-10 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Имя автора")),
                (
                    "link",
                    models.CharField(
                        max_length=200, verbose_name="Ссылка на страницу автора"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hab",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Заголовок")),
                (
                    "link",
                    models.CharField(
                        max_length=200,
                        unique=True,
                        verbose_name="Ссылка на страницу хаба",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(verbose_name="Дата создания")),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                (
                    "link",
                    models.CharField(
                        max_length=200,
                        unique=True,
                        verbose_name="Ссылка на страницу статьи",
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст статьи")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.author",
                        verbose_name="Автор",
                    ),
                ),
                (
                    "hab",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.hab",
                        verbose_name="Хаб",
                    ),
                ),
            ],
        ),
    ]
