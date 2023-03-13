from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)