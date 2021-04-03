from django.urls import path

from articles.views import ArticleList, ArticleCreate, ArticleDetail

app_name = 'article'

urlpatterns = [
    path('', ArticleList.as_view()),
    path('create/', ArticleCreate.as_view()),
]
