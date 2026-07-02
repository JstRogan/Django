from datetime import datetime, timezone

from django.db import migrations

from articles.data import ARTICLES, CATEGORIES


def seed(apps, schema_editor):
    Category = apps.get_model("articles", "Category")
    Article = apps.get_model("articles", "Article")

    categories = {}
    for name in CATEGORIES:
        categories[name], _ = Category.objects.get_or_create(name=name)

    for item in ARTICLES:
        article, created = Article.objects.get_or_create(
            title=item["title"],
            defaults={
                "author": item["author"],
                "image": item["image"],
                "category": categories[item["category"]],
                "content": item["content"],
                "likes": item["likes"],
                "dislikes": item["dislikes"],
            },
        )
        if created:
            created_at = datetime.strptime(item["created_at"], "%Y-%m-%d")
            Article.objects.filter(pk=article.pk).update(
                created_at=created_at.replace(tzinfo=timezone.utc)
            )


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
