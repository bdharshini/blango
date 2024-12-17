from django.shortcuts import render
from blog.models import post
from django.utils import timezone
def index(request):
  posts=post.objects.filter(published_at__lte=timezone.now())
  return render(request,"blog/index.html",{"post":posts})
# Create your views here.
