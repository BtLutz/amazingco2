from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("nodes/", views.NodeCreate.as_view()),
    path("nodes/<int:pk>/", views.NodeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
