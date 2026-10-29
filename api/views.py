import io
from .models import Person
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import GenericAPIView
from .serializers import PersonSerializer, PersonModelSerializer
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# @api_view(['GET','PUT','PATCH'])
# def singleobj(request,id):
#     data = get_object_or_404(Person, id=id)

#     if request.method ==  "PUT":
#         parsed_data = request.data
#         serializer = PersonModelSerializer(data, data = parsed_data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"update":"successful!"},status=status.HTTP_200_OK)

#     if request.method == "PATCH":
#         parsed_data = request.data
#         serializer = PersonModelSerializer(data, data = parsed_data, partial = True) 
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"update":"successful!"},status=status.HTTP_200_OK)
 

#     if request.method == "GET":
#         serializer = PersonModelSerializer(data)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type = 'application/json')

# @api_view(['GET','POST'])
# def multipleobj(request):


#     if request.method == "POST":
#         parsed_data = request.data
#         serializer = PersonModelSerializer(data = parsed_data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"update":"successful!"},status=status.HTTP_200_OK)
    
#     if request.method == "GET":
#         data = Person.objects.all()
#         serializer = PersonModelSerializer(data, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type = 'application/json')


class SingleObjAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

class MultipleObjAPIView(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        return self.create(request)

    def get(self, request, *args, **kwargs):
        # print(request.user)
        return self.list(request, *args, **kwargs)