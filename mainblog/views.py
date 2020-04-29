from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Post,Extrapages
import random
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method=="GET":
        form=websiteusers_register()
        counttotalpost=Post.objects.all().count()
        slice = random.random() * (counttotalpost - 5)
        bannerpost = Post.objects.all()[slice:slice+6]
        slice = random.random() * (counttotalpost - 3)


        # Body Post Fetch And Adding Some Custom Fields
        bodypost = Post.objects.all()[slice:slice + 10]
        bodypost = list(bodypost)
        count = 0
        for i in bodypost:
            addc = count + 1
            bodypost[count].count = addc
            slug_url = bodypost[count].post_titel
            slug_url = slug_url.replace(" ", "-")
            bodypost[count].url = slug_url
            timemin=random.randint(1,20)
            bodypost[count].time=timemin
            count = count + 1

        #side Post Fetch And Adding Some Custom Fields
        sidepost = Post.objects.all()[slice:slice + 4]
        sidepost=list(sidepost)
        count=0
        for i in sidepost:
            addc=count+1
            sidepost[count].count = addc
            slug_url=sidepost[count].post_titel
            slug_url=slug_url.replace(" ","-")
            sidepost[count].url=slug_url
            count=count+1


        data={'posts':bannerpost,'bodyposts':bodypost,'sideposts':sidepost,'form':form}
        return render(request,"mainblog/index.html",data)


def postdetails(request,id,titel):
    if request.method=="GET":
        form=post_comments_form()
        titel=titel.replace("-"," ")
        post=Post.objects.filter(id=id,post_titel=titel)
        counttotalpost = Post.objects.all().count()
        slice = random.random() * (counttotalpost - 5)


        # side Post Fetch And Adding Some Custom Fields
        sidepost = Post.objects.all()[slice:slice + 10]
        sidepost = list(sidepost)
        count2 = 0
        for i in sidepost:
            addc = count2 + 1
            sidepost[count2].count = addc
            slug_url = sidepost[count2].post_titel
            slug_url = slug_url.replace(" ", "-")
            sidepost[count2].url = slug_url
            count2=count2 + 1

            # Body Post Fetch And Adding Some Custom Fields
            bodypost = Post.objects.all()[slice:slice + 3]
            bodypost = list(bodypost)
            count3 = 0
            for i in bodypost:
                addc = count3 + 1
                bodypost[count3].count = addc
                slug_url = bodypost[count3].post_titel
                slug_url = slug_url.replace(" ", "-")
                bodypost[count3].url = slug_url
                timemin = random.randint(1, 20)
                bodypost[count3].time = timemin
                count3 = count3 + 1
        postcomments=Post_Comment.objects.filter(post=id)
        senddata={"postdetails":post,"sideposts":sidepost,"bodyposts":bodypost,'form':form,'postcomments':postcomments}
        return render(request,"mainblog/detail.html",senddata)


    if request.method=="POST":
        form=post_comments_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
        else:

            return HttpResponseRedirect(request.path_info)


def contact(request):
    if request.method=="POST":
        form = Contact_query(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, 'Thanks You. We Will Get Back You Soon. ')
            form = Contact_query()
            form = {"form": form}
            return render(request, "mainblog/contact.html", form)
        else:
            messages.error(request, 'Please Enter The Correct Informations')
            form = Contact_query()
            form = {"form": form}
            return render(request,"mainblog/contact.html",form)

    else:
        form = Contact_query()
        form = {"form": form}

        return render(request, "mainblog/contact.html", form)


def about(request,pname):
     
    about=Extrapages.objects.filter(slug=pname)
    print(about)
    data={"about":about}
    return render(request,"mainblog/about-us.html",data)


