from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update

app_name = "leads"
urlpatterns = [
    path('lead_list/', lead_list, name="all"),
    path('lead_detail/<int:pk>/', lead_detail, name="lead_detail"),
    path('lead_create/', lead_create, name="lead_create"),
    path('lead_update/<str:pk>/', lead_update, name="lead_update"),
]
