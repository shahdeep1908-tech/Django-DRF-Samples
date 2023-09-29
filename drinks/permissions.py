from rest_framework import permissions


class AuthenticateCreateAndAllowList(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)


class AuthenticateDrinkDetails(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return True


class OnlyAdminAccessUserList(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class OnlyParticularAdminAccessUserDetail(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.id == request.user.id
