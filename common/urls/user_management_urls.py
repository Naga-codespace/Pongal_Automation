
from django.urls import path

from common.views.user_management_views import (
    UserListCreateAPIView,
    RoleListCreateAPIView,
    PermissionListAPIView,
    UserRoleMappingAPIView,
    RolePermissionMappingAPIView,
    UserListHTMLView,
    UserCreateHTMLView
)

urlpatterns = [

    ##API endpoints for user management, role management, permission management, and their mappings
    # User management
    path("users/", UserListCreateAPIView.as_view(),
         name="user-list-create"),


    # Role management
    path("roles/", RoleListCreateAPIView.as_view(),
         name="role-list-create"),

    # Permission management
    path("permissions/", PermissionListAPIView.as_view(),
         name="permission-list"),

    # User-role mapping
    path("users/<int:user_id>/roles/",
         UserRoleMappingAPIView.as_view(),
         name="user-role-mapping"),

    # Role-permission mapping
    path("roles/<int:role_id>/permissions/",
         RolePermissionMappingAPIView.as_view(),
         name="role-permission-mapping"),

#######################################
     path("users/list/html",UserListHTMLView.as_view(),name="user_list_html"),
     path("users/create/html",UserCreateHTMLView.as_view(),name="user_create_html")
]
