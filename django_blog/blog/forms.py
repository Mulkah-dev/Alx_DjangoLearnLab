from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']

# ✅ User Update Form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Author will be set automatically in views

    # Optional: Add some styling using widgets
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your content...'}),
    }