from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from collection.serializers.collection import CollectionSerializer
from collection.services.collections import create_collection
from collection.models.collections import Collection


class CollectionCreateAPIView(APIView):
    def post(self, request):
        print(request.data)
        serializer = CollectionSerializer(
            data=request.data
        )
      
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

class CollectionDetailAPIView(APIView):

    def get(self, request, pk):

        try:
            collection = Collection.objects.get(pk=pk)

        except Collection.DoesNotExist:
            return Response(
                {"error": "Collection not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

class CollectionDeleteAPIView(APIView):

    def delete(self, request, pk):
        try:
            collection = Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            return Response(
                {"error": "Collection not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        collection.delete()
        return Response(
            {"message": "Collection deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )    


class CollectionUpdateAPIView(APIView):

    def put(self, request, pk):
        try:
            collection = Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            return Response(
                {"error": "Collection not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CollectionSerializer(
            collection,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )    