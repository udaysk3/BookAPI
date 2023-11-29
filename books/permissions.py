from rest_framework import permissions

class IsEmailVerified(permissions.BasePermission):
    message = 'Email verification is required to access this resource.'

    def has_permission(self, request, view):
        # Allow access to unauthenticated users (e.g., for registration)
        if request.user.is_anonymous:
            return True

        # Allow access if the user is verified
        return request.user.is_verified