from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Post, Comment, Tag

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
    new_tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas"
    )
    class Meta:
        model = Post
        fields = ['title', 'content']  # Author will be set automatically in views

    # Optional: Add some styling using widgets
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your content...'}),
    }
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()

        # Handle tags
        tags_str = self.cleaned_data.get('new_tags', '')
        if tags_str:
            tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                post.tags.add(tag)

        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only the comment text should be entered by the user

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            }),
        }
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content.strip()) < 2:
            raise forms.ValidationError("Comment is too short.")
        return content