from django import forms
from . import models

"""
class for creating custom django forms for custom article data fields
"""

class createArticle(forms.ModelForm):
    class Meta:
        # fields from articles model
        model = models.Articles
        fields = ['title', 'content', 'slug', 'thumbnail']