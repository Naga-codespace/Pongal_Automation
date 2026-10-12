from django.db.models.aggregates import Sum,Count
from django.shortcuts import render
from django.http import JsonResponse
from collection.models.collections import Collection


def login_page(request):
    # Logic for handling login page
    return render(request,'coreui/authentication/login.html')  # Redirect to collection list page after login


def log_out_page(request):
    # Logic for handling logout page
    return render(request,'coreui/authentication/log_out.html')  # Redirect to collection list page after login

def test_function(request):
    collections =  Collection.objects.aggregate(total = Count('id'))
    return JsonResponse({'message': 'Test function executed successfully.', 'collections': collections})