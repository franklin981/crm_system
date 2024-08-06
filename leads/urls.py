from django.urls import path
from .views import lead_list, lead_detail

app_name = "leads"
urlpatterns = [
    path('leads/', lead_list, name="all"),
    path('lead_detail/<int:pk>/', lead_detail, name="lead_detail")
]
