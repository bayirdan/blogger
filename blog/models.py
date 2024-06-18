from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(null=False, blank=True, unique=True, editable=False, db_index=True)

  def __str__(self):
    return f"{self.name}"
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super().save(*args, **kwargs)

class Blog(models.Model):
  title = models.CharField(max_length=100)
  blogger = models.CharField(max_length=100, default='admin', null=False)
  description = models.TextField()
  imageFile = models.ImageField(upload_to='uploads/', null=False, blank=True)
  isActive = models.BooleanField(default=False)
  isHome = models.BooleanField(default=False)
  slug = models.SlugField(null=False, blank=True, editable=False, unique=True, db_index=True)
  category = models.ForeignKey(Category, blank=True, on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.title}"
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)

