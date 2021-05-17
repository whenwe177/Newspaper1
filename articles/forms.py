from django import forms
from .models import Article,Comment

#class NewArticleForm(forms.Form):
    #title = forms.CharField(max_length=70)
    #body = forms.CharField(widget=forms.Textarea)

#class NewArticleForm(forms.ModelForm):
    #class Meta:
        #model = Article
        #fields = (
            #"title",
            #"body",
        #)

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "title",
            "body",
        )

    def editSave(self,commit=True):
        article = self.instance
        article.title = self.cleaned_data["title"]
        article.body = self.cleaned_data["body"]

        if commit:
            article.save()
        return article

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "comment",
        )

    def editSave(self,commit=True):
        comment = self.instance
        comment.comment = self.cleaned_data["comment"]

        if commit:
            comment.save()
        return comment