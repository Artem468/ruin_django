from django.contrib import admin

from core.models import Tour, ScheduledTour, Point, Entry


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'price', 'max_members')
    list_display_links = ('name',)
    search_fields = ('name', 'place')
    list_filter = ('place',)


@admin.register(ScheduledTour)
class ScheduledTourAdmin(admin.ModelAdmin):
    list_display = ('tour', 'start_at', 'end_at', 'guide')
    list_display_links = ('tour',)
    search_fields = ('tour__name', 'guide')
    list_filter = ('start_at', 'guide')


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('name', 'tour', 'number')
    list_display_links = ('name',)
    search_fields = ('name', 'tour__name')
    list_filter = ('tour',)
    ordering = ('tour', 'number')


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'scheduled_tour', 'telegram_id', 'name', 'email',
        'phone', 'is_need_lunch', 'is_need_notify', 'count_members'
    )
    list_display_links = ('scheduled_tour',)
    search_fields = ('name', 'email', 'phone', 'telegram_id')
    list_filter = ('is_need_lunch', 'is_need_notify', 'scheduled_tour')