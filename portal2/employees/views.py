from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Employee, Position, Department
from .serializers import *


@api_view(['GET', 'POST'])
def employee_list(request):
    # list all employees
    if request.method == 'GET':
        data = []
