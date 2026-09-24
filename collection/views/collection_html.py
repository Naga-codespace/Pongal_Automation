from django.shortcuts import render


def collection_page(request):
    return render(
        request,
        "collection/create.html"
    )