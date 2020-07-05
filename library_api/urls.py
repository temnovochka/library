from django.conf.urls import url
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from library_api.views import BookViewSet, AuthorViewSet, FollowerViewSet, LanguageViewSet, BookSearchList

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register(r'language', LanguageViewSet)
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'follower', FollowerViewSet)
urlpatterns = router.urls

urlpatterns += [
    url(r'^search/', BookSearchList.as_view(), name='search'),
    url(r'^schema/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
