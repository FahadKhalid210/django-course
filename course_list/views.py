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
            filters['display_name__icontains'] = disp_name
        
        if lang := request.GET.get('lang'):
            filters['language__icontains'] = lang
        
        serialized_courses = [] 
        courses_queryset =  CourseOverview.get_all_courses(filter_=filters)
        for course in courses_queryset:
            # Serialize each course and append to the list
            serialized_courses.append({
                'name': course.display_name,
                'language': course.language,
                'start_date': course.start,
                'end_date': course.end,
                # Add any other fields that you want to include
            })
            
        return Response(serialized_courses)
