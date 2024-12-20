from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone
from django.shortcuts import redirect
from blog.forms import CommentForm
def index(request):
  p=post.objects.filter(published_at__lte=timezone.now())
  return render(request,"blog/index.html",{"posts":p})

def post_detail(request,slug):
  p=get_object_or_404(post,slug=slug)
  if request.user.is_active:
    if request.method == "POST":
      comment_form = CommentForm(request.POST)

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = p
        comment.creater = request.user
        comment.save()
        return redirect(request.path_info)
    else:
        comment_form = CommentForm()
  else:
      comment_form = None
  return render(request,"blog/post-details.html",{"post":p,"comment_form":comment_form})