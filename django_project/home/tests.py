from django.core.urlresolvers import reverse
from django.test import TestCase

from home.models import Theme
from article.models import Article


class HomeViewTests(TestCase):

    # Test response when the admin has no theme objects
    def test_index_view_with_no_theme(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.context.get("theme"), None)

    # Test response when there are theme objects, but none are selected as the current theme
    def test_index_view_with_false_current_theme(self):
        Theme.objects.create(theme_name="test", current_theme=False)
        Article.objects.create(game_name="test", published_status=True)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.context.get("theme"), None)

    # Test response when there are no articles published
    def test_index_view_with_no_articles(self):
        Theme.objects.create(theme_name="test", current_theme=True)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.context.get("theme"), None)

    # Test response with articles and current theme object
    def test_index_view_with_correct_context(self):
        theme_test_object = Theme.objects.create(theme_name="test", current_theme=True)
        Article.objects.create(game_name="test", published_status=True)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get("theme"), theme_test_object)
        self.assertQuerysetEqual(response.context.get("current_articles"), ["<Article: test>"])