from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP Methods as function(get,post,patch,put,delete)'
        'Is Similar to a traditional Django view',
        'Gives you the most control over you application logic',
        'Is Mapped Manually to Urls'
        ]
        return Response({'message': 'Hello','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello name with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
             )
