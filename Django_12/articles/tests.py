from django.test import TestCase
from django.urls import reverse

from articles.models import Article, ArticleReaction, Category


IMAGE_URL = "https://res.cloudinary.com/demo/image/upload/sample.jpg"


class News12Tests(TestCase):
    def setUp(self):
        self.category = Category.objects.get(slug="programming")
        self.article = Article.objects.create(
            title="Python article",
            author="Student",
            image_url=IMAGE_URL,
            category=self.category,
            excerpt="Short preview",
            content="Full article",
        )

    def test_article_list_and_detail_work(self):
        list_response = self.client.get(reverse("articles:list"))
        detail_response = self.client.get(
            reverse("articles:detail", kwargs={"slug": self.article.slug})
        )

        self.assertContains(list_response, "Python article")
        self.assertContains(list_response, 'name="value" value="like"')
        self.assertContains(list_response, 'name="value" value="dislike"')
        self.assertContains(detail_response, "Full article")

    def test_article_create_form(self):
        response = self.client.post(
            reverse("articles:create"),
            {
                "title": "Design article",
                "author": "Designer",
                "image_url": IMAGE_URL,
                "category": self.category.id,
                "excerpt": "Preview",
                "content": "Content",
            },
        )

        article = Article.objects.get(title="Design article")
        self.assertRedirects(response, reverse("articles:detail", kwargs={"slug": article.slug}))

    def test_like_dislike_updates_single_session_reaction(self):
        self.client.post(
            reverse("articles:react", kwargs={"slug": self.article.slug}),
            {"value": "like"},
        )
        self.client.post(
            reverse("articles:react", kwargs={"slug": self.article.slug}),
            {"value": "dislike"},
        )

        self.assertEqual(ArticleReaction.objects.count(), 1)
        self.assertEqual(ArticleReaction.objects.get().value, ArticleReaction.DISLIKE)
