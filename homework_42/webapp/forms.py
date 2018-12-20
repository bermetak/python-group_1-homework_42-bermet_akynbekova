from django import forms
from webapp.models import Article, Comment


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

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'article', 'autor', 'comment'}

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'comment'}