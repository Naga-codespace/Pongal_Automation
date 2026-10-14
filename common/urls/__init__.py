from common.urls.common_urls import urlpatterns as common_urlpatterns
from common.urls.user_management_urls import urlpatterns as user_management_urlpatterns

urlpatterns = common_urlpatterns + user_management_urlpatterns