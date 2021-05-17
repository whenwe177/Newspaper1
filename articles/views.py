from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm,NewCommentForm
from .models import Article,Comment

# Create your views here.
def viewArticle(response):
    articleLst = Article.objects.all()
    return render(response,"articles/viewarticle.html",{"lst":articleLst})

def detailArticle(response,id):
    article = Article.objects.get(id=id)
    commentLst = article.comment.all
    return render(response,"articles/detailarticle.html",{"article":article,"lst":commentLst})

def postArticle(response):
    if not response.user.is_authenticated:
        return redirect("/login")

    if response.method == "POST":
        form = NewArticleForm(response.POST)
        if form.is_valid():
            #title = form.cleaned_data["title"]
            #body = form.cleaned_data["body"]
            
            #post = Article(title=title,body=body)
            post = form.save(commit=False)
            post.author = response.user
            post.save()

            return redirect("/viewarticles")
    else:
        form = NewArticleForm()
    return render(response,"articles/create.html",{"form":form})


def editArticle(response,id):
    article = Article.objects.get(id=id)
    if response.method == "POST":
        form = NewArticleForm(response.POST or None,instance=article)
        if form.is_valid():
            obj = form.editSave(commit=False)
            obj.save()
            article = obj
            return redirect(f"/article/{id}")
    else:
        form = NewArticleForm(initial =
            {
                "title" : article.title,
                "body" : article.body,
            }
        )
    return render(response,"articles/edit.html",{"form":form,"article":article}) 

def delArticle(response,id):
    article = Article.objects.get(id=id)

    if response.method == "POST":
        article.delete()
        return redirect("/viewarticles")

    return render(response,"articles/delete.html",{"article":article})

def addComment(response,id):
    if not response.user.is_authenticated:
        return redirect("/login")

    article = Article.objects.get(id=id)

    if response.method == "POST":
        form = NewCommentForm(response.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            
            comment.author = response.user
            comment.article = article
            comment.save()

            return redirect("/viewarticles")
    else:
        form = NewCommentForm()

    return render(response,"articles/addcomment.html",{"form":form})

def editComment(response,id):
    comment = Comment.objects.get(id=id)
    article = comment.article
    if response.method == "POST":
        form = NewCommentForm(response.POST,instance=comment)
        if form.is_valid():
            obj = form.editSave(commit=False)
            obj.author = response.user
            obj.save()
            
            return redirect(f"/article/{article.id}")
    else:
        form = NewCommentForm(
            initial = {
                "comment" : comment.comment,
            }
        )
    return render(response,"articles/editcomment.html",{"form":form})

def delComment(response,id):
    comment = Comment.objects.get(id=id)
    article = comment.article
    
    if response.method == "POST":
        comment.delete()
        return redirect(f"/article/{article.id}")
    
    return render(response,"articles/deletecomment.html",{})

