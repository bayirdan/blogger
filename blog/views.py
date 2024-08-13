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

  categories_list = []

  for category in categories:
    blogs_by_category = Blog.objects.filter(category = category.id)
    category_length = len(blogs_by_category)
    categories_list.append({
      'name': category.name,
      'length': category_length,
      'slug': category.slug
    })

  context = {
    "blogs": blogs,
    "categories": categories,
    "categories_list": categories_list,
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

    blog = Blog.objects.create(title=title, category=category, isHome=is_home, isActive=is_active, description=blogText, blogger=blogger)

    if image != None:
      blog.imageFile = image

    blog.save()
    return redirect("home")
  
  return render(request, "blog/create-blog.html", {"categories": categories})

def edit_blog(request, slug):
  if request.user.is_authenticated == None:
    return redirect("blogs")
  
  categories = Category.objects.all()
  blog = Blog.objects.get(slug = slug)

  if request.method == 'POST':

    title = request.POST["title"]
    categoryID = request.POST["category"]
    blogText = request.POST["blogText"]
    is_active = request.POST.get("is_active")
    is_home = request.POST.get("is_home")
    image = request.FILES.get("fileImage")

    if is_active == "True":
      is_active = True
    else:
      is_active = False

    if is_home == "True":
      is_home = True
    else:
      is_home = False

    if categoryID != "all":
      category = Category.objects.get(id=categoryID)
    else:
      category = blog.category

    if not title:
      return render(request, "blog/edit-blog.html", {
        "title": "",
        "blogText": blogText,
        "title_error": "Title is required",
        "categories": categories,
        "category": category,
        "is_active": is_active,
        "is_home": is_home,
        "blogger": blog.blogger,
      })
    
    if not blogText:
      return render(request, "blog/edit-blog.html", {
        "blogText": "",
        "title": title,
        "blog_text_error": "Blog Text is required",
        "categories": categories,
        "category": category,
        "is_active": is_active,
        "is_home": is_home,
        "blogger": blog.blogger,
      })

    if image != None:
      blog.image = image

    print(image)

    blog.title = title
    blog.description = blogText
    blog.isActive = is_active
    blog.isHome = is_home
    blog.category = category
    blog.save()

    return redirect("user_blogs", blog.blogger)


  context = {
    "title": blog.title,
    "categories": categories,
    "category": blog.category,
    "blogText": blog.description,
    "is_active": blog.isActive,
    "is_home": blog.isHome,
    "blogger": blog.blogger,
    "image": blog.imageFile,
    "slug": blog.slug
  }

  return render(request, 'blog/edit-blog.html', context)

def delete_blog(request, slug):
  if request.user.is_authenticated == None:
    return redirect("blogs")
  
  blog = Blog.objects.get(slug = slug)

  if request.user.username == blog.blogger:
    blog.delete()

  return redirect("blogs")

def filter_category(request, slug):
  blogs = Blog.objects.filter(category__slug = slug)
  categories = Category.objects.all()

  categories_list = []

  for category in categories:
    blogs_by_category = Blog.objects.filter(category = category.id)
    category_length = len(blogs_by_category)
    categories_list.append({
      'name': category.name,
      'length': category_length,
      'slug': category.slug
    })

    
  context = {
    "blogs": blogs,
    "categories": categories,
    "selected_category": slug,
    "categories_list": categories_list
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
