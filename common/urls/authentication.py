from django.urls import path

from common.views.authentication import test_function
from common.views.dashboard import dashboard
urlpatterns = [

      path("dashboard/",
            dashboard,
            name="dashboard"),
      path("test_api/",
            test_function,
            name="test_function")
]