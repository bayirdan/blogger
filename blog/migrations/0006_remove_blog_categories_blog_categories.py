# Generated by Django 4.1.5 on 2024-04-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blog_categories_blog_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='categories',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, default=1, to='blog.category'),
        ),
    ]
