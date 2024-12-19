from django.contrib.auth import get_user_model
from django import template
from blog.models import post
from django.utils.html import escape
from django.utils.html import format_html
from django.utils.safestring import mark_safe
register=template.Library()
user_model=get_user_model()#get user model instance
#custom filter to return first and lastname else username as a link so that they can be emailed to when clicked
#used formatting for escaping and providing safe data to include in html
@register.filter
def author_details(author,current_user):
  if not isinstance(author,user_model):
    return ""
  if author==current_user:
    return format_html("<strong>Me</strong>")
  if author.first_name and author.last_name:
    name=escape(f"{author.first_name} {author.last_name}")
  else:
    name=escape(f"{author.username}")

  if author.email:
    prefix=format_html('<a href="mailto:{}">',author.email)
    suffix=format_html("</a>")
  else:
    preifx=""
    suffix=""
  return format_html('{}{}{}',prefix,name,suffix)
#custom tags for row and endrow
@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row {}">',extra_classes)
  
@register.simple_tag
def endrow():
  return format_html('</div>')

@register.inclusion_tag("blog/post-list.html")
def recent_posts(posts):
  p=post.objects.exclude(pk=posts.pk)[:5]
  return {"title":"Recent posts","post":p}#always returns back a dictonary item


