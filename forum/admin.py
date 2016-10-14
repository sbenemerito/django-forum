from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "date_added", "author"]
	list_filter = ('date_added', 'author')
	search_fields = ['title']

	class Meta:
		model = Post


class CommentModelAdmin(admin.ModelAdmin):
	list_display = ["post", "date_added", "author"]
	list_filter = ('date_added', 'author', 'post')

	class Meta:
		model = Comment


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)