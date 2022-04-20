from fileinput import filename
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Prob
from .serializers import ProbSerializer
from django.core.files.storage import FileSystemStorage
from gridfs import GridFS
from utils import get_db_handle

db, client = (get_db_handle())
collection = db['projectop']

# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/probs/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of scripts'
        },
        {
            'Endpoint': '/probs/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single script object'
        },
        {
            'Endpoint': '/probs/create/',
            'method': 'POST',
            'body': {'body': {}},
            'description': 'Creates new script with data sent in post request'
        },
        {
            'Endpoint': '/probs/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing script with data sent in post request'
        },
        {
            'Endpoint': '/file/upload/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a script'
        },
        {
            'Endpoint': '/probs/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting script'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def getProbs(request):
    probs = Prob.objects.all().order_by('-updated')
    serializer = ProbSerializer(probs, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProb(request, pk):
    prob = Prob.objects.get(id=pk)
    serializer = ProbSerializer(prob, many=False)
    return Response(serializer.data)


# @api_view(['POST'])
# def createProb(request):
#     data = request.data
#     fs = GridFS(db)
#     image = fs.put(data['image'])
#     # print(fs.get(image))

#     collection.insert_one({
#         'image': image,
#         'location': {"hehe": "haha"},
#     })
#     # return Response(serializer.data)
    # return Response('uploaded!', status=200)


@api_view(['POST'])
def createProb(request):
    data = request.data
    print("data", data)
    prob = Prob.objects.create(
        image=data['image'],
        location={
            'latitude': data['latitude'],
            'longitude': data['longitude'],
        }
    )
    serializer = ProbSerializer(prob, many=False)
    return Response(serializer.data)


@ api_view(['PUT'])
def updateProb(request, pk):
    data = request.data
    prob = Prob.objects.get(id=pk)
    serializer = ProbSerializer(instance=prob, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@ api_view(['DELETE'])
def deleteProb(request, pk):
    script = Prob.objects.get(id=pk)
    script.delete()
    return Response('Prob was deleted!')


# @api_view(['POST'])
# def uploadFile(request):

#     data = request.data
#     file = File.objects.create(
#         name='works!',
#         filestore=data['file']
#     )
#     fs = FileSystemStorage()
#     res = FileSerializer.data
#     print('asd', request)
#     # context['url'] = fs.url(name)

#     return Response('File Added')
