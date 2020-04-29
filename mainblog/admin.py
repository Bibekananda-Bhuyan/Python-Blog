from django.contrib import admin
from  .models import Blog_Category,Post,Websiteuser,Extrapages,Contactquery,Post_Comment
 # Register your models here.
admin.site.register(Blog_Category)
admin.site.register(Post)
admin.site.register(Websiteuser)
admin.site.register(Extrapages)
admin.site.register(Contactquery)
admin.site.register(Post_Comment)
