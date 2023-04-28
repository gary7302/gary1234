from django.contrib.auth.forms import UserCreationForm
from .models import User,ChinaComment,HindiComment,Comment,SpanishComment
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Your Password'}))
    class Meta:
        model=User
        fields=['email','password1','password2']


class CommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=Comment
        fields=['comment_body','comment_image']

class ChinaCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=ChinaComment
        fields=['comment_body','comment_image']

class HindiCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=HindiComment
        fields=['comment_body','comment_image']

class SpanishCommentForm(forms.Form):

    comment_body = forms.CharField(widget=forms.Textarea)
    #product_id = forms.IntegerField(widget=forms.HiddenInput)
    comment_image=forms.ImageField(required=False)
    class Meta:
        model=SpanishComment
        fields=['comment_body','comment_image']