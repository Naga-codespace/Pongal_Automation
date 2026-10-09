from django.shortcuts import redirect


def login_page(request):
    # Logic for handling login page
    return redirect(request,'coreui/authentication/login.html')  # Redirect to collection list page after login