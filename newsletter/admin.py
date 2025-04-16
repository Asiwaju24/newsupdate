from django.contrib import admin
from .models import Newsletter, Subscriber

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'sender_email')
    search_fields = ('title', 'description')
    list_filter = ('owner',)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscriber, SubscriberAdmin)