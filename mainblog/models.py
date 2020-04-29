from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog_Category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    post_titel=models.CharField(max_length=1000)
    post_category=models.ForeignKey(Blog_Category,on_delete=models.CASCADE,null=True)
    post_banner_image=models.ImageField(upload_to="mainblog/static/mainblog/media")
    post_content=RichTextField()
    is_comment_allows=models.BooleanField("Is Comment Allow",default=True)


    def __str__(self):
        return self.post_titel


class Websiteuser(models.Model):
    useremail=models.CharField(max_length=300,unique=True)
    name=models.CharField(max_length=300)
    password=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Extrapages(models.Model):
    titel=models.CharField(max_length=300)
    slug=models.CharField(max_length=200,default="")
    content=RichTextField()

    def __str__(self):
        return self.titel

class Contactquery(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=500)
    subject=models.CharField(max_length=1000)
    massage=RichTextField()
    is_contacted=models.BooleanField("Is Contacted",default=False)

    def __str__(self):
        return self.name


class Post_Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=300)
    useremail=models.CharField(max_length=500)
    comment=models.TextField(max_length=5000)
    added_date=models.DateField(auto_now=True)


