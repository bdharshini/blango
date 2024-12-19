from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone
def index(request):
  p=post.objects.filter(published_at__lte=timezone.now())
  return render(request,"blog/index.html",{"posts":p})

def post_detail(request,slug):
  p=get_object_or_404(post,slug=slug)
  return render(request,"blog/post-details.html",{"post":p})