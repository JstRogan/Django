from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    author = models.CharField(max_length=80)
    image_url = models.URLField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="articles")
    excerpt = models.TextField(max_length=420)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})

    @property
    def likes_count(self):
        return self.reactions.filter(value=ArticleReaction.LIKE).count()

    @property
    def dislikes_count(self):
        return self.reactions.filter(value=ArticleReaction.DISLIKE).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "article"
            slug = base_slug
            counter = 2
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class ArticleReaction(models.Model):
    LIKE = "like"
    DISLIKE = "dislike"
    CHOICES = [(LIKE, "Like"), (DISLIKE, "Dislike")]

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="reactions")
    session_key = models.CharField(max_length=40)
    value = models.CharField(max_length=10, choices=CHOICES)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["article", "session_key"],
                name="unique_session_reaction",
            )
        ]

    def __str__(self):
        return f"{self.article} - {self.value}"
