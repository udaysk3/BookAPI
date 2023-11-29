# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer,PartialBookUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsEmailVerified
from .models import CustomUser
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE'] 
    permission_classes = [IsAuthenticated, IsEmailVerified]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)    

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PartialBookUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_verification_email(user_id=user.username, user_email=user.email)

        return Response({"message": "User created successfully. Check your email for verification."},
                        status=status.HTTP_201_CREATED)

# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_verification_email(user_id, user_email):
    subject = 'Verify your email'
    message = f'Click the link to verify your email: http://127.0.0.1:8000/verify?username={user_id}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)


class EmailVerificationView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user_id = self.request.query_params.get('username')
        permission_classes = []
        # print(user_id, CustomUser.objects.get(username="uday"))
        try:
            user = CustomUser.objects.get(username=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "Invalid user ID"}, status=status.HTTP_400_BAD_REQUEST)

        user.is_verified = True
        user.save()

        return Response({"detail": "Email verification successful"}, status=status.HTTP_200_OK)

