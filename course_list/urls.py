"""
URLs for course_list.
"""
from django.urls import re_path, path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

from .views import GetCourses, GetCoursesV2

urlpatterns = [
    path('fahad/', GetCourses.as_view(), name='get-courses'),
    path('fahad2/', GetCoursesV2.as_view(), name='get-courses-v2'),
]