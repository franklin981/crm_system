from django.urls import path
from .views import homepage, feedback

app_name = "leads"
urlpatterns = [
    path('all/', homepage, name="all"),
    path('second/', feedback, name="feedback")
]
