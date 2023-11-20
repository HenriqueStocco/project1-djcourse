from django.contrib import admin
from .models import Category, Recipe

# Register your models here.
# @admin.register e o mesmo que admin.site.register(model, adminclass)


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
