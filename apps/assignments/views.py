from django.shortcuts import render,get_object_or_404,redirect
from .serializers import AssignmentSerializer
from .models import Assignment
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView


class ListCreateAPIView(generics.ListCreateAPIView):
    """
        This generic class list's all courses and create's a new course 
    """
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()


create_List_view = ListCreateAPIView.as_view()

class AssignementDetail(APIView):
    """ A view that get's a specified user course by looking up an id  """
    def get(self,request,pk = None):
        if pk is not None:
            qs = get_object_or_404(Assignment,id = pk)        # qs = Course.objects.get(id = pk)
            serializer = AssignmentSerializer(qs)
            return Response(serializer.data)
        return Response({"error":"Invalid request"},status=400)
detail_view = AssignementDetail.as_view()



class DeleteAPIView(generics.DestroyAPIView):
    """
        A class that delete's an existing course 
    """
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    lookup_field = "pk"

    def get_object(self):
        # Use the primary key (pk) to retrieve the object
        obj = super().get_object()

        
        return obj
        
        
        


delete_view = DeleteAPIView.as_view()



class UpdateAPIView(generics.UpdateAPIView):
    """ 
    this class alters existing instance of the object/course 
     
    """

    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
        
    #     response = self.update(request, *args, **kwargs)
    #     # if response.status_code == status.HTTP_200_OK:
    #     #     return self.redirect_view()
        
    #     return response
        
    # def redirect_view(self):
    #     return redirect('/assignment/list/')
        
        
update_view = UpdateAPIView.as_view()


