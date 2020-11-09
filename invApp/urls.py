from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('', views.index),
    path('addBook',views.addBook),
    path('authorPage', views.authorPage),
    path('addAuthor', views.addAuthor),
    path('singleBook/<int:myVal>', views.singleBook),
    path('appendAuthor/<int:bookId>', views.appendAuthor),
    path('singleAuthor/<int:myVal>', views.singleAuthor),
    path('appendBook/<int:authorId>', views.appendBook)
]