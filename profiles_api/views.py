from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
        "Uses HTTP Methods as function{get, post, patch,, put, delete}",
        "Is similar to a traditional Django view",
        "Gives you the most control over your application logic",
        "Is Mapped manually to URLs",
        ]
        return Response({'message':'hello!', 'an_apiview':an_apiview})
