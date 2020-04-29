from django import forms
from .models import Websiteuser,Post_Comment,Contactquery


class websiteusers_register(forms.ModelForm):
    name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"frm-input","placeholder":"Name"}),required=True)
    email=forms.EmailField(max_length=300,widget=forms.TextInput(attrs={"class":"frm-input","placeholder":"Email"}),required=True)
    password=forms.CharField(max_length=300,widget=forms.TextInput(attrs={"class":"frm-input","placeholder":"Password"}),required=True)

    class Meta():
        model=Websiteuser
        fields=['name','useremail','password']


class post_comments_form(forms.ModelForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "frm-input", "placeholder": "Name"}),
                           required=True)
    useremail = forms.EmailField(max_length=300,
                             widget=forms.TextInput(attrs={"class": "frm-input", "placeholder": "Email"}),
                             required=True)
    comment = forms.CharField(max_length=3000,
                                 widget=forms.Textarea(attrs={"class": "frm-input", "placeholder": "Comment"}),
                                 required=True)

    class Meta():
        model=Post_Comment
        fields=['username','useremail','comment','post']


class Contact_query(forms.ModelForm):
    name = forms.CharField(max_length=200,
                               widget=forms.TextInput(attrs={"class": "frm-input", "placeholder": "Name"}),
                               required=True)
    email = forms.EmailField(max_length=200,
                           widget=forms.TextInput(attrs={"class": "frm-input", "placeholder": "Email"}),
                           required=True)
    subject = forms.CharField(max_length=300,
                                 widget=forms.TextInput(attrs={"class": "frm-input", "placeholder": "Subject"}),
                                 required=True)
    massage = forms.CharField(max_length=3000,
                              widget=forms.Textarea(attrs={"class": "frm-input", "placeholder": "Comment"}),
                              required=True)
    class Meta():
        model=Contactquery
        fields=["name","email","subject","massage"]
