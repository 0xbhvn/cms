from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

from articles.models import Article
from articles.serializers import ArticleSerializer


@permission_classes([IsAuthenticated, ])
class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@permission_classes([IsAuthenticated, ])
class ArticleListSearch(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title', 'body', 'author__username', 'category']


@permission_classes([IsAdminUser, ])
class ArticleCreate(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        author = Article(author=request.user)
        serializer = ArticleSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated, ])
class ArticleDetail(APIView):
    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug, format=None):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article)

        return Response(serializer.data)


@permission_classes([IsAdminUser, ])
class ArticleUpdateDelete(APIView):
    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, slug, format=None):
        article = self.get_object(slug)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        article = self.get_object(slug)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
