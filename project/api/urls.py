from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('places_at/<str:coords>', views.places_at, name="places-at"),
    url(r'^', include(router.urls)),
]