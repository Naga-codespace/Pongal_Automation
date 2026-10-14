from django.shortcuts import render
from django.http import JsonResponse
from django.views import View as view

from common.services import charts_service as collection_services_charts


class DashboardService(view):
    def get(self,request):
        return render(request, 'dashboard.html')  

class ChartsData(view):
    def get(self, request, *args, **kwargs):
        chart_type = kwargs.get('chart_type')
        if chart_type == 'daily-collection':
            return self.daily_collection(request)
        elif chart_type == 'payment-mode':
            return self.payment_mode(request)
        return JsonResponse({'error': 'Invalid chart type'}, status=400)

    def daily_collection(self, request):
        chart_data = collection_services_charts.get_daily_collection_chart_data()
        return JsonResponse(chart_data)

    def payment_mode(self, request):
        chart_data = collection_services_charts.get_payment_details_chart_data()
        return JsonResponse(chart_data)