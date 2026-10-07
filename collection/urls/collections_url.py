from django.urls import path

from collection.views.collection_api import CollectionCreateAPIView,CollectionListAPIView,CollectionDetailAPIView,CollectionDeleteAPIView, CollectionUpdateAPIView
from collection.views.collection_html import collection_create,collection_list


urlpatterns = [
    #create ->>>>>>>>>page
    path(
        "create/api",
        CollectionCreateAPIView.as_view(),
        name="collection-create-api"
    ),
    path(
        "create/html",
        collection_create,
        name="collection-create-page"
    ),
    #list ->>>>>>>>>page
    path(
        "list/api",
        CollectionListAPIView.as_view(),
        name="collection-list-api"
    ),
    path(
        "list/html",
        collection_list,
        name="collection-list-page"
    ),
    #details ->>>>>>>>>page
    path("detail/api/<int:pk>",
         CollectionDetailAPIView.as_view(),
         name="collection-detail-api"),
    #delete ->>>>>>>>>page
    path("delete/api/<int:pk>",
         CollectionDeleteAPIView.as_view(),
         name="collection-delete-api"),
    #update ->>>>>>>>>page
    path("update/api/<int:pk>",
         CollectionUpdateAPIView.as_view(),
         name="collection-update-api"),

]