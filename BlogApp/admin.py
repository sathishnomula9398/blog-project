from django.contrib import admin
from BlogApp.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug', 'author', 'publish', 'created', 'updated','status']
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={"slug":('title',)}
    raw_id_fields=('author',)
    ordering=['status','publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','body','created','updated','active','post')
    list_filter = ('created','active','updated')
    search_fields = ('name','email','body')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

