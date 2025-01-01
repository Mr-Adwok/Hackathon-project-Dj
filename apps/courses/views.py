from django.shortcuts import render,get_object_or_404,redirect
from .serializers import CourseSerializer
from .models import Course
from rest_framework import generics,status
from rest_framework.response import Response


# a create class that creates Courses
class CreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


create_view = CreateAPIView.as_view()

class ListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


list_view = ListAPIView.as_view()

class DeleteAPIView(generics.DestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = "pk"

    def get_object(self):
        # Use the primary key (pk) to retrieve the object
        obj = super().get_object()

        
        return obj
        return redirect('Course/list/')
        
        
        


delete_view = DeleteAPIView.as_view()



class UpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
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
    #     return redirect('/Course/list/')
        
        
update_view = UpdateAPIView.as_view()


