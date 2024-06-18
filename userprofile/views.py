from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog.models import Blog

# Create your views here.

def get_profile(request):
  if not request.user.is_authenticated:
    return redirect('register')

  user_data = request.user

  blogs = Blog.objects.filter(blogger=user_data.username)

  context = {
    'blogs': blogs,
    'date_joined': user_data.date_joined,
    'last_login': user_data.last_login,
    'email': user_data.email,
    'username': user_data.get_username(),
    'fullname': user_data.get_full_name(),
  }
  
  return render(request, 'userprofile/profile.html', context)

def edit_profile(request):
  if not request.user.is_authenticated:
    return redirect("register")
  else:
    context = {
      'username': request.user.username,
      'email': request.user.email,
      'first_name': request.user.first_name,
      'last_name': request.user.last_name
    }

    if request.method == 'POST':
      email = request.POST["email"]
      first_name = request.POST["first_name"]
      last_name = request.POST["last_name"]
      password = request.POST["password"]

      if password == '' or email == '' or first_name == '' or last_name == '':
        return render(request, "userprofile/editprofile.html", 
          {"error": "Tüm field'ler dolu olmalı!",
          'username': request.user.username,
          'email': request.user.email,
          'first_name': request.user.first_name,
          'last_name': request.user.last_name
        })

      if not request.user.check_password(password):
        return render(request, "userprofile/editprofile.html", 
          {"error": "Parola hatalı!",
          'username': request.user.username,
          'email': request.user.email,
          'first_name': request.user.first_name,
          'last_name': request.user.last_name
        })
      
      if User.objects.filter(email=email).exclude(pk=request.user.pk).exists():
        return render(request, "userprofile/editprofile.html", 
          {"error": "Bu email adresi zaten kullanılıyor!",
          'username': request.user.username,
          'email': request.user.email,
          'first_name': request.user.first_name,
          'last_name': request.user.last_name
        })
      else:
        request.user.email = email
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()
        return render(request, "userprofile/editprofile.html", 
          {"success": "Profil başarıyla güncellendi",
          'username': request.user.username,
          'email': request.user.email,
          'first_name': request.user.first_name,
          'last_name': request.user.last_name
        })
    return render(request, "userprofile/editprofile.html", context)
