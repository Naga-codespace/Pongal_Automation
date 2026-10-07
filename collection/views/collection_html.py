from django.http import request
from django.shortcuts import render


def collection_create(request):
    return render(
        request,
        "collection/create.html"
    )

def collection_list(request):
    return render(
        request,
        "collection/list.html"
    )

def collection_money_receipt(request, pk):
    return render(
        request,
        "collection/money_receipt.html",{'pk':pk}
    )   