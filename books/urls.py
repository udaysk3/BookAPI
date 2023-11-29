# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import UserRegistrationView, EmailVerificationView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('verify', EmailVerificationView.as_view(), name='verify_email'),
]
