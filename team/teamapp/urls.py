from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from teamapp import views

urlpatterns = [
    path('members/', views.MemberList.as_view()),
    path('members/<int:pk>/', views.MemberDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)