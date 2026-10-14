
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_active",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]
        read_only_fields = ["id"]


class PermissionSerializer(serializers.ModelSerializer):
    module = serializers.CharField(
        source="content_type.app_label",
        read_only=True,
    )
    model_name = serializers.CharField(
        source="content_type.model",
        read_only=True,
    )

    class Meta:
        model = Permission
        fields = [
            "id",
            "name",
            "codename",
            "module",
            "model_name",
        ]


class UserRoleMappingSerializer(serializers.Serializer):
    role_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        allow_empty=True,
    )

    def validate_role_ids(self, value):
        if len(value) != len(set(value)):
            raise serializers.ValidationError(
                "Duplicate role IDs are not allowed."
            )

        found_ids = set(
            Group.objects.filter(pk__in=value)
            .values_list("pk", flat=True)
        )

        if found_ids != set(value):
            raise serializers.ValidationError(
                "One or more role IDs do not exist."
            )

        return value


class RolePermissionMappingSerializer(serializers.Serializer):
    permission_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        allow_empty=True,
    )

    def validate_permission_ids(self, value):
        if len(value) != len(set(value)):
            raise serializers.ValidationError(
                "Duplicate permission IDs are not allowed."
            )

        found_ids = set(
            Permission.objects.filter(pk__in=value)
            .values_list("pk", flat=True)
        )

        if found_ids != set(value):
            raise serializers.ValidationError(
                "One or more permission IDs do not exist."
            )

        return value
