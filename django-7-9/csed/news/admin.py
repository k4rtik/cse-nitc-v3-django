from csed.news.models import NewsItem
from django.contrib import admin

class NewsItemAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['heading', 'category', 'sub_category']}),
		('Details', {'fields':['content', 'attachment']}),
		('Publishing Options', {'fields':['published']}),
        ]
	list_display = ('heading', 'category', 'sub_category', 'pub_time', 'published')
	list_filter = ['category', 'sub_category', 'published', 'pub_time']
	search_fields = ['heading', 'content']
	date_hierarchy = 'pub_time'
	actions_on_top = False
	actions_on_bottom = True
admin.site.register(NewsItem, NewsItemAdmin)
