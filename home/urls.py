from django.urls import path

from . import views
from analytics.views import RecordUserAction


urlpatterns = [
    path("", views.index, name="index"),
    path('record/', RecordUserAction.as_view(), name='record_user_action')
]
