from django.urls import path
from .views import UserFilterView

urlpatterns = [
    path('', UserFilterView.as_view(), name='user_filter'),
    # Add other URL patterns if needed
]
