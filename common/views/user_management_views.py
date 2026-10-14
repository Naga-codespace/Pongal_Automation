
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from common.serlizers import (
    UserSerializer,
    RoleSerializer,
    PermissionSerializer,
    UserRoleMappingSerializer,
    RolePermissionMappingSerializer,
)

User = get_user_model()


# 1. USER MANAGEMENT: list and create users
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


# 2. ROLE MANAGEMENT: list and create roles
class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all().order_by("name")
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]


# 3. PERMISSION MANAGEMENT: list available permissions
class PermissionListAPIView(generics.ListAPIView):
    queryset = Permission.objects.select_related(
        "content_type"
    ).order_by("content_type__app_label", "codename")
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminUser]


# 4. USER-ROLE MAPPING
class UserRoleMappingAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)

        roles = user.groups.all().order_by("name")

        return Response({
            "user_id": user.pk,
            "username": user.get_username(),
            "roles": RoleSerializer(roles, many=True).data,
        })

    def put(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)

        serializer = UserRoleMappingSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        role_ids = serializer.validated_data["role_ids"]
        roles = Group.objects.filter(pk__in=role_ids)

        # Replace all roles with the submitted list.
        user.groups.set(roles)

        return self.get(request, user_id)


# 5. ROLE-PERMISSION MAPPING
class RolePermissionMappingAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, role_id):
        role = get_object_or_404(Group, pk=role_id)

        permissions = role.permissions.select_related(
            "content_type"
        ).order_by("codename")

        return Response({
            "role_id": role.pk,
            "role_name": role.name,
            "permissions": PermissionSerializer(
                permissions, many=True
            ).data,
        })

    def put(self, request, role_id):
        role = get_object_or_404(Group, pk=role_id)

        serializer = RolePermissionMappingSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        permission_ids = serializer.validated_data[
            "permission_ids"
        ]
        permissions = Permission.objects.filter(
            pk__in=permission_ids
        )

        # Replace all permissions with the submitted list.
        role.permissions.set(permissions)

        return self.get(request, role_id)
