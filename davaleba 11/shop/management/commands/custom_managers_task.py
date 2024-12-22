from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = Category.objects.with_item_count()
        for category in categories:
            print(f"{category.name}: {category.item_count} items")

        items = Item.objects.with_tag_count()
        for item in items:
            print(f"{item.name}: {item.tags_count} tags")

        min_items = 2
        popular_tags = Tag.objects.popular_tags(min_items=min_items)
        for tag in popular_tags:
            print(f"{tag.name}: {tag.item_count} items")