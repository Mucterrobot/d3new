from django.urls import path
from.views import *


urlpatterns = [
    path('authorList', AuthorList.as_view()),
    path('post/', Post.as_view()),
    path('postCreate/', PostCreate.as_view()),

]
