from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Blog, Category

# Create your views here.

def index(request):
  blogs = Blog.objects.filter(isHome=True, isActive=True)
  context = {
    "blogs": blogs
  }
  return render(request, "blog/index.html", context)

def blogs(request):
  blogs = Blog.objects.filter(isActive=True)
  categories = Category.objects.all()
  context = {
    "blogs": blogs,
    "categories": categories
  }
  return render(request, "blog/blogs.html", context)

def blog_detail(request, slug):
  blog = Blog.objects.get(slug = slug)
  
  return render(request, "blog/blog-detail.html", {
    "blog": blog
  })

def create_blog(request):
  if request.user.is_authenticated == None:
    return redirect("blogs")
  
  categories = Category.objects.all()
  if request.method == "POST":
    title = request.POST["title"]
    categoryID = request.POST["category"]
    blogText = request.POST["blogText"]
    is_active = request.POST.get("is_active")
    is_home = request.POST.get("is_home")
    blogger = request.user.username
    image = request.FILES.get("fileImage")

    if categoryID != "all":
      category = Category.objects.get(id=categoryID)

    if is_active == "True":
      is_active = True
    else:
      is_active = False

    if is_home == "True":
      is_home = True
    else:
      is_home = False

    if not title:
      return render(request, "blog/create-blog.html", {
        "title": "",
        "blogText": blogText,
        "title_error": "Title is required",
        "categories": categories
      })
    
    if not blogText:
      return render(request, "blog/create-blog.html", {
        "blogText": "",
        "title": title,
        "blog_text_error": "Blog Text is required",
        "categories": categories
      })
    
    blog = Blog.objects.create(title=title, category=category, isHome=is_home, isActive=is_active, description=blogText, blogger=blogger, imageFile=image)
    blog.save()
    return redirect("home")
  return render(request, "blog/create-blog.html", {"categories": categories})

def filter_category(request, slug):
  blogs = Blog.objects.filter(category__slug = slug)
  category_length = len(blogs)
  categories = Category.objects.all()
  context = {
    "blogs": blogs,
    "categories": categories,
    "selected_category": slug,
    "category_length": category_length,
  }
  return render(request, "blog/blogs.html", context)

def get_user_blogs(request, username):
  blogs = Blog.objects.filter(blogger = username)

  if len(blogs) == 0:
    return redirect('blogs')

  context = {
    'blogs': blogs,
    'username': username,
  }

  return render(request, 'blog/user-blogs.html', context)
