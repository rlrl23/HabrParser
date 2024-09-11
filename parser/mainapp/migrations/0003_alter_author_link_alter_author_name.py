# Generated by Django 4.2.3 on 2024-09-10 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_alter_article_options_alter_author_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="link",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Ссылка на страницу автора"
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Имя автора"
            ),
        ),
    ]
