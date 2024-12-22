from django.contrib import admin
from .models import Category, Item, Tag

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [ItemInline]

class TagInline(admin.StackedInline):
    model = Item.tags.through
    extra = 0
    verbose_name = "Tag"
    verbose_name_plural = "Tags"

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    search_fields = ('name', 'description')
    ordering = ('-price',)
    inlines = [TagInline]

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.register(Category)
admin.register(Tag)
admin.register(Item)