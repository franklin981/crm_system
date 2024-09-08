from django.urls import path
# from .views import (lead_list, lead_detail, lead_create, lead_update, landing_page, lead_delete,
#         LandingPageView, LeadListView
#)
from django.conf import settings
from django.conf.urls.static import static
from .views import (LeadUpdateView,
        LandingPageView, LeadListView, LeadCreateView, LeadDetailView, LeadDeleteView
)

app_name = "leads"

urlpatterns = [
    path('lead_list/', LeadListView.as_view(), name="lead_list"),
    path('lead_detail/<int:pk>/', LeadDetailView.as_view(), name="lead_detail"),
    path('lead_create/', LeadCreateView.as_view(), name="lead_create"),
    path('lead_update/<str:pk>/', LeadUpdateView.as_view(), name="lead_update"),
    path('lead_delete/<str:pk>/', LeadDeleteView.as_view(), name='lead_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)