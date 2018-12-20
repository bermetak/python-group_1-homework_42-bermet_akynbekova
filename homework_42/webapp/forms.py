from django import forms
from webapp.models import Article


class ArticleSearchForm(forms.Form):
    article_title = forms.CharField(required=False, max_length=200, label='Поиск статьи')

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = {'autor', 'title', 'content'}

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = {'title', 'content'}