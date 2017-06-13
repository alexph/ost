from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import ReactionEntry, ImageReaction, TweetReaction


class ReactionEntryInline(GenericTabularInline):
    model = ReactionEntry
    min_num = 1
    max_num = 1


class GenericReactionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'deleted']
    inlines = [
        ReactionEntryInline
    ]


admin.site.register(ImageReaction, GenericReactionAdmin)
admin.site.register(TweetReaction, GenericReactionAdmin)
