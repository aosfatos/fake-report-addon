from django.urls import path
from api import views as api_views


urlpatterns = [
    path('create/', api_views.EventCreateView.as_view(), name='event_create'),
    path('blacklist/', api_views.BlackListView.as_view(), name='blacklist'),
]
