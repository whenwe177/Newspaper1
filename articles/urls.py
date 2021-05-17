from django.urls import path,include
from . import views

urlpatterns = [
    path("create/",views.postArticle,name="postArticle"),
    path("viewarticles/",views.viewArticle,name="viewArticle"),
    path("article/<int:id>/",views.detailArticle,name="detailArticle"),
    path("article/<int:id>/edit/",views.editArticle,name="editArticle"),
    path("article/<int:id>/delete/",views.delArticle,name="delArticle"),
    path("article/<int:id>/addcomment/",views.addComment,name="addComment"),
    path("article/comment/<int:id>/edit/",views.editComment,name="editComment"),
    path("article/comment/<int:id>/delete/",views.delComment,name="delComment"),

]