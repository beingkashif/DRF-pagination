from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .pagination import LimitOffsetPagination

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    pagination_class = LimitOffsetPagination

