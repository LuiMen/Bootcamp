from rest_framework.permissions import BasePermission

from apps.user.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == User.Type.ADMIN


class IsEditorial(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == User.Type.EDITORIAL


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == User.Type.AUTOR
