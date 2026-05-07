from django.test import TestCase
from django.urls import reverse

from articles.models import Article, Category


class ModelsHomeworkTests(TestCase):
    def setUp(self):
        self.category = Category.objects.get(slug="backend")

    def test_article_and_category_models_work(self):
        article = Article.objects.create(
            title="Models lesson",
            author="Student",
            image_url="https://res.cloudinary.com/demo/image/upload/sample.jpg",
            category=self.category,
            excerpt="Preview",
            content="Content",
        )

        self.assertEqual(str(article), "Models lesson")
        self.assertEqual(str(self.category), "Backend")
        self.assertEqual(article.slug, "models-lesson")

    def test_article_list_page_uses_models(self):
        Article.objects.create(
            title="Admin article",
            author="Teacher",
            image_url="https://res.cloudinary.com/demo/image/upload/sample.jpg",
            category=self.category,
            excerpt="Preview",
            content="Content",
        )

        response = self.client.get(reverse("articles:list"))

        self.assertContains(response, "Admin article")
