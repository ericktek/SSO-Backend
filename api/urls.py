from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SchoolViewSet, StudentViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
