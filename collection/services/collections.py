from django.utils import timezone
from collection.models.collections import Collection


def create_collection(validated_data):
    if 'date' not in validated_data:
        validated_data['date'] = timezone.now()

    collection = Collection.objects.create(
        **validated_data
    )
    collection.token = collection.token_number()
    collection.save(update_fields=["token"])
    return collection