from django.urls import path
# from .views import (lead_list, lead_detail, lead_create, lead_update, landing_page, lead_delete,
#         LandingPageView, LeadListView
#)
from .views import (lead_detail, lead_create, lead_update, lead_delete,
        LandingPageView, LeadListView
)

app_name = "leads"

urlpatterns = [
    path('lead_list/', LeadListView.as_view(), name="lead_list"),
    path('lead_detail/<int:pk>/', lead_detail, name="lead_detail"),
    path('lead_create/', lead_create, name="lead_create"),
    path('lead_update/<str:pk>/', lead_update, name="lead_update"),
    path('lead_delete/<str:pk>/', lead_delete, name='lead_delete'),
]