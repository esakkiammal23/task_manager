from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Task
from.serializers import Task2

@api_view(['POST'])
def add(request):
    serializer = Task2(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def get_tasks(request):
    tasks=Task.objects.all()
    serializer = Task2(tasks,many=True)
    return Response(serializer.data)



@api_view(['PUT'])
def update(request,pk):
    task=Task.objects.get(id=pk)
    task.task_status=request.data.get('task_status')
    task.save()
    serializer=Task2(task)
    return Response(serializer.data)




@api_view(['DELETE'])
def delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response({
        "message":"Deleted"
    })
    