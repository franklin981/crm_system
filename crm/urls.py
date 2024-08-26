from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('leads/', include('leads.urls', namespace='leads')),
    path('', LandingPageView.as_view(), name='home' ),
]
