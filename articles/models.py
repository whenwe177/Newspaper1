from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="article",null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail",args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comment")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="comment",null=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("article_list")