# Generated by Django 5.0.4 on 2024-06-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_blog_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imageFile',
            field=models.ImageField(blank=True, default='no-image.png', upload_to='uploads/'),
        ),
    ]
