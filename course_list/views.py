from rest_framework.views import APIView
from rest_framework.response import Response

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview


class GetCourses(APIView):
    def get(self, request):
        message = {'message': 'Hello, world!'}
        return Response(message)


class GetCoursesV2(APIView):
    def get(self, request):
        filters = {}
        if disp_name := request.GET.get('name'):
            filters['display_name'] = disp_name
        
        if lang := request.GET.get('lang'):
            filters['language'] = lang

        queryset =  CourseOverview.get_all_courses(filter_=filters)
        return Response(list(queryset.values()))
