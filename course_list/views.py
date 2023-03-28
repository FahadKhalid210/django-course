from rest_framework.views import APIView
from rest_framework.response import Response

class GetCourses(APIView):
    def get(self, request):
        message = {'message': 'Hello, world!'}
        return Response(message)