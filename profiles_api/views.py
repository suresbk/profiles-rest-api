from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):


    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods(GET, POST, PUT, PATCH, DELETE)',
            'Similar to traditional Django view',
            'Most control over Applicaiton Logic',
            'Mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    

    