from django.contrib import admin

from apps.anime.models import Anime, AnimeSeason


class AnimeSeasonInline(admin.TabularInline):
    model = AnimeSeason
    extra = 0


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "season_amount",)
    inlines = (AnimeSeasonInline,)


@admin.register(AnimeSeason)
class AnimeSeasonAdmin(admin.ModelAdmin):
    list_display = ("name", "number")
    # inlines = (AnimeSeasonInline,)
