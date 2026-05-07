from django.db import migrations


def seed_categories(apps, schema_editor):
    Category = apps.get_model("articles", "Category")
    for name, slug in [
        ("Programming", "programming"),
        ("Design", "design"),
        ("Backend", "backend"),
        ("Frontend", "frontend"),
    ]:
        Category.objects.get_or_create(slug=slug, defaults={"name": name})


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_categories, migrations.RunPython.noop),
    ]
