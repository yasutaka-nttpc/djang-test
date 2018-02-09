from rest_framework import viewsets, routers
from myapp.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
  serializer_class = ArticleSerializer

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
