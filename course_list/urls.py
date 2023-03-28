"""
URLs for course_list.
"""
from django.urls import re_path, path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

from .views import GetCourses

urlpatterns = [
    path('api/getcourses/', GetCourses.as_view(), name='get-courses'),
]