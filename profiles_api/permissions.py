from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow user to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit profiel"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """allow usr to upadate their own status"""

    def has_object_permission(self, request, view, obj):
        """used to check user is trying to upadte their own stsaus"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
            
