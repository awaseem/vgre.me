from django.core.urlresolvers import reverse
from django.test import TestCase

from home.models import Theme
from article.models import Article
from users.models import User


def create_test_theme():
    return Theme.objects.create(theme_name="test", current_theme=True)


def create_test_user():
    return User.objects.create_user("test")


def create_test_article():
    return Article.objects.create(game_name="test", published_status=True, created_user="test")


class ArticleViewTests(TestCase):

    def test_article_call_with_no_articles(self):
        create_test_theme()
        create_test_user()
        response = self.client.get(reverse("article", args=["test"]))
        self.assertEqual(response.status_code, 404)

    def test_article_call_with_no_theme(self):
        create_test_user()
        create_test_article()
        response = self.client.get(reverse("article", args=["test"]))
        self.assertEqual(response.status_code, 404)

    def test_article_call_with_no_user(self):
        create_test_article()
        create_test_theme()
        response = self.client.get(reverse("article", args=["test"]))
        self.assertEqual(response.status_code, 404)

    def test_article_call_with_correct_context(self):
        create_test_theme()
        create_test_user()
        create_test_article()
        response = self.client.get(reverse("article", args=["test"]))
        self.assertEqual(response.status_code, 200)

    def test_search_with_results(self):
        create_test_theme()
        create_test_article()
        response = self.client.post(reverse("search"), {"search_query": "test"})
        self.assertEqual(response.status_code, 302)