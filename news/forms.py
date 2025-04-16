
from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'author', 'category', 'trending']
    
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'})
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 80, 'class': 'form-control'}))
    
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
    
    author = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'})
    )
    
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

  
    trending = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
