from django.urls import path

from common.views.authentication_views import test_function
from common.views.dashboard_views import ChartsData, DashboardService
urlpatterns = [

      path("dashboard/",
            DashboardService.as_view(),
            name="dashboard"),
      path("charts-data/<str:chart_type>/",
            ChartsData.as_view(),
            name="charts_data"),
      path("test_api/",
            test_function,
            name="test_function")
]