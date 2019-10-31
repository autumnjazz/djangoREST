from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from mystorage import views

router = DefaultRouter()
router.register('essay', views.PostViewSet)
router.register('album', views.ImgViewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]

