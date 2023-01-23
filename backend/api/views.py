from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient
from bson.json_util import dumps, loads
from .crud import CRUD
from rest_framework.decorators import api_view

crud = CRUD()

def wrapRespond(respond):
    return 'OK' if respond.acknowledged == True else 'NOT OK'

# Create your views here.
def test(request):
    return JsonResponse('this is a test', safe=False)

@api_view(['GET'])
def get_all_info(request):
    raw_data = crud.get_all()
    json_data = dumps(list(raw_data))
    return JsonResponse(json_data, safe=False)

@api_view(['POST'])
def create_info(request):
    data = request.data
    insert_resp = crud.create(data)
    return JsonResponse(wrapRespond(insert_resp),safe=False)

@api_view(['PUT'])
def update_info(request):
    data = request.data
    update_resp = crud.update(data)
    return JsonResponse(wrapRespond(update_resp),safe=False)


@api_view(['DELETE'])
def delete_info(request):
    data = request.data
    delete_resp = crud.remove(data)
    return JsonResponse(wrapRespond(delete_resp),safe=False)
