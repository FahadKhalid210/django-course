from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from openedx.core.djangoapps.content.course_overviews.serializers import CourseOverviewBaseSerializer


class GetCourses(APIView):
    def get(self, request):
        message = {'message': 'Hello, world!'}
        return Response(message)


class GetCoursesV2(ListAPIView):
    serializer_class = CourseOverviewBaseSerializer

    def get_queryset(self):
        filters = {}
        if disp_name := self.request.query_params.get('name'):
            filters['display_name__icontains'] = disp_name
        
        if lang := self.request.query_params.get('lang'):
            filters['language__icontains'] = lang
        
        return CourseOverview.get_all_courses(filter_=filters)
