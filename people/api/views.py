from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from people.models import Visitor,People
from .serializer import VisitorSerializer
from .utils import sendMail


@api_view(['POST','GET'])
def add_visitor(request):
    ''' api for adding visitors '''

    if request.method == 'GET':
        try:
            visitors = Visitor.objects.all()
            serializer = VisitorSerializer(visitors,many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    elif request.method=='POST':
        serializer = VisitorSerializer(data = request.data)
        if request.data['temp']>37:
            people = People.objects.get(id = request.data['name'])
            info = {
                'name':people.name,
                "temp":request.data['temp']
            }
            sendMail(info)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)