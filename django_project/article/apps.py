from django.apps import AppConfig
import watson


class ArticleConfig(AppConfig):
    name = "article"

    def ready(self):
        # Tells what watson what model to search within
        Article = self.get_model("Article")
        # Configures Watson to only search pub=True entries and add front, back and description to meta
        watson.register(Article.objects.filter(published_status=True),
                        store=("game_name", "game_review_cover", "game_review_back_cover", "game_review_description"))