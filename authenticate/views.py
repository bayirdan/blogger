from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
  if request.user.is_authenticated:
    return redirect("home")
  else:
    if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]

      user = authenticate(request, username=username, password=password)

      if user is None:
        return render(request, "authenticate/login.html", {
          "error": "username ya da password hatalı!"
        })
      
      login(request, user)
      return redirect("home")
    
    return render(request, "authenticate/login.html")

def logout_view(request):
  logout(request)
  return redirect('home')

def register_view(request):
  if request.user.is_authenticated:
    return redirect("home")
  
  if request.method != "POST":
    return render(request, "authenticate/register.html")
  
  username = request.POST["username"]
  email = request.POST["email"]
  first_name = request.POST["first_name"]
  last_name = request.POST["last_name"]
  password = request.POST["password"]
  repassword = request.POST["repassword"]
  
  if password != repassword:
    return render(request, "authenticate/register.html",
      {"error": "paralolar eşleşmiyor!",
      "username": username,
      "email": email,
      "first_name": first_name,
      "last_name": last_name
    })
  
  if User.objects.filter(email = email).exists():
    return render(request, "authenticate/register.html",
      {"error": "Bu email zaten kullanılıyor!",
      "username": username,
      "email": email,
      "first_name": first_name,
      "last_name": last_name
    })
  
  if User.objects.filter(username = username).exists():
    return render(request, "authenticate/register.html",
      {"error": "Bu username kullanılıyor!",
      "username": username,
      "email": email,
      "first_name": first_name,
      "last_name": last_name
    })
  
  user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
  user.save()
  return redirect("login")
    
  #  Giriş yapma ve kayıt olma kısımları tamamlandı, burdan sonrası sende