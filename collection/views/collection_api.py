from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from collection.serializers.collection import CollectionSerializer
from collection.services.collections import create_collection
from collection.models.collections import Collection


class CollectionCreateAPIView(APIView):
    def post(self, request):
        serializer = CollectionSerializer(
            data=request.data
        )
        print(serializer)
        print(serializer.data)

        serializer.is_valid(
            raise_exception=True
        )
        collection = create_collection(
            serializer.validated_data
        )
        response_serializer = CollectionSerializer(
            collection
        )
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )


class CollectionListAPIView(APIView):

    def get(self, request):

        collections = Collection.objects.all()
        serializer = CollectionSerializer(
            collections,
            many=True
        )

        return Response(serializer.data)
    