from django.contrib import admin
from blog.models import Tag,post
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields={"slug":("title",)}
  list_display=("slug","content")
admin.site.register(post,PostAdmin)
# Register your models here.
