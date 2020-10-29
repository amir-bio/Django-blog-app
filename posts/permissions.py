from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #  read-only permissions granted for any request
        # write permissions are only granted if the caller is the author
        return bool(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
