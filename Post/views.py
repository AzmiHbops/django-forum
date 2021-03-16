from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post
from taggit.models import Tag
from django.db.models import Count

# Create your views here.

#Home view - index.html
def home(request, tag_slug=None):
    posts = Post.objects.filter(status='published')
    tag = None
    if  tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    context = {"posts":posts, "tag":tag}
    return render(request, "post/index.html", context)


#For post details
def detail(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(status='published', tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-published')[:4]
    context = {"post":post, 'similar_posts':similar_posts}
    return render(request, "post/details.html", context)


#Create new blog-post
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        detail = request.POST.get('detail')
        status = request.POST.get('status')

        if title and detail:
            p = Post.objects.create(title=title, slug=slug, detail=detail, status=status, author=request.user)
            return redirect(p.get_absolute_url())
    return render(request, "post/create.html")

    
#Edit blog-post
def edit(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    context = {'post':post}
    if request.method == "POST":
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        status = request.POST.get('status')

        if title and detail:
            post.title=title
            post.detail=detail
            post.status=status
            post.save()
            return redirect(post.get_absolute_url())
        
    return render(request, "post/edit.html", context)


#Delete blog-post (Admins only)
def delete(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    context = {'post':post}
    if request.method == "POST":
        post.delete()
        return redirect("post:home")
        
    return render(request, "post/delete.html", context)

