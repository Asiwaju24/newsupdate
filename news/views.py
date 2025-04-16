from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
def home(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'post': post})
    
def error(request):
	return render(request, 'error.html', {})

def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    related_posts = Post.objects.filter(category=post.category).exclude(id=pk)[:3] 
    return render(request, 'post.html', {'post': post, 'related_posts': related_posts})

def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        post = Post.objects.filter(category=category)
        return render(request, 'category.html', {'post': post, 'category': category})
    except Category.DoesNotExist:
        messages.error(request, "Category does not exist.")
        return redirect('home')

def create_post(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your post has been created successfully.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = PostForm()
        return render(request, 'create_post.html', {'form': form})
    else:
        messages.error(request, "Access Denied")
        return redirect('home')

def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        post = Post.objects.all()
        return render(request, 'dashboard.html', {'post': post})
    else:
        return redirect('error')

def delete_post(request):
    if request.POST.get('action') == 'post':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        post.delete()
        return JsonResponse({"message": "Post deleted successfully"})