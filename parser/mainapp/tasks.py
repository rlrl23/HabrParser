import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import logging
from mainapp.models import Author, Article, Hab

from parser.celery import app

logger = logging.Logger(name="task")


@app.task
def task_one():
    ua = UserAgent()

    headers = {
        "accept": "application/json, text/plain, */*",
        "user-Agent": ua.google,
    }

    articles = []
    habs = Hab.objects.all()

    for hab in habs:
        url = hab.link
        req = requests.get(url, headers=headers).text
        soup = BeautifulSoup(req, "lxml")
        all_articles = soup.find_all(
            "div", class_="tm-article-snippet"
        )  # получаем статьи

        for article in all_articles:
            author = article.find("a", class_="tm-user-info__username")
            author_name = author.text
            author_link = f'https://habr.com{author.get("href")}'
            author, created = Author.objects.get_or_create(
                name=author_name, link=author_link
            )

            created_at_a = article.find("a", class_="tm-article-datetime-published")
            created_at = created_at_a.find("time").get("datetime")
            article_a = article.find("a", class_="tm-title__link")
            article_name = article_a.find("span").text
            article_link = f'https://habr.com{article_a.get("href")}'
            req = requests.get(article_link, headers=headers).text
            soup = BeautifulSoup(req, "lxml")
            text = soup.find("div", class_="article-formatted-body").text
            articles.append(
                Article(
                    title=article_name,
                    link=article_link,
                    text=text,
                    created_at=created_at,
                    author=author,
                    hab=hab,
                )
            )
        try:
            Article.objects.bulk_create(articles, ignore_conflicts=True)
        except Exception as e:
            logger.error(str(e))
    return "success"
