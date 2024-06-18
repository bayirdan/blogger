from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/create", views.create_blog, name="create-blog" ),
    path("blogs/<slug:slug>", views.blog_detail, name="blog-detail"),
    path("blogs/user/<str:username>", views.get_user_blogs, name="get-user-blogs"),
    path("category/<slug:slug>", views.filter_category, name="filter-category")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
