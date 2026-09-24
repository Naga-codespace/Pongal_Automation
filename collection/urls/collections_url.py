from django.urls import path

from collection.views.collection_api import CollectionCreateAPIView
from collection.views.collection_html import collection_page


urlpatterns = [

    # REST API
    path(
        "api/collections/",
        CollectionCreateAPIView.as_view(),
        name="collection-create-api"
    ),
    # HTML page
    path(
        "collection/create/",
        collection_page,
        name="collection-page"
    ),
]