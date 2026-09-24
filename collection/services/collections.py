from collection.models.collections import Collection



def create_collection(validated_data):
    collection = Collection.objects.create(
        **validated_data
    )
    collection.token = collection.token_number()
    collection.save(update_fields=["token"])
    return collection