from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"cart", CartViewSet)
router.register(r"order", OrderViewSet)
router.register(r"order-product", OrderProductViewSet)
router.register(r"review", ReviewViewSet)


urlpatterns = [
    # backend
    path("admin/", admin.site.urls),
    path("api/", include(router.urls), name="api"),
    # auth
    path("api/drf-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # frontend
    path("", about, name="about"),
    path("catalog/", catalog, name="catalog"),
    path("review/", review, name="review"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
