__author__ = 'narcis'

from django import forms
from models import Article,Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model=Article
        fields=['title','content','thumbnail']

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=['content']
    '''
    def clean(self):
        cleaned_data=self.cleaned_data


        return cleaned_data
    '''