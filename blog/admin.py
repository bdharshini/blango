from django.contrib import admin
from blog.models import Tag,post,Comment
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields={"slug":("title",)}
  list_display=("slug","content")
admin.site.register(post,PostAdmin)
admin.site.register(Comment)
# Register your models here.
