"""
course_list Django application initialization.
"""

from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import ProjectType
from edx_django_utils.plugins import PluginURLs


class CourseListConfig(AppConfig):
    """
    Configuration for the course_list Django application.
    """

    name = 'course_list'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'course_list',
                PluginURLs.REGEX: r'^api/course_list/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }
