from .views import TagViewSet, EntryViewSet, ArticleViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'tags', TagViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = router.urls
