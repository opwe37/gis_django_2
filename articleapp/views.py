from django.forms import ModelForm
from django.shortcuts import render

# Create your views here.
from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']
