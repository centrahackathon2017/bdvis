from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    context = {}
    return render(request, "index.html", context)


def example_json_response(request):
    data = {"foo": "bar", "listdata": [1, 2, 3]}
    return JsonResponse(data)
