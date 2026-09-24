from rest_framework import serializers
from collection.models.collections import Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            "id",
            "person_name",
            "mobile_number",
            "amount",
            'collection_date',
            "payment_mode",
            "token",
            "collector_name",
            "payment_status",
            "date",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "token",
            "created_at",
        ]

    def validate_amount(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Amount must be greater than zero."
            )

        return value