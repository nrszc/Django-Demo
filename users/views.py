from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.models import BookInfo


def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    print("99999")
    return HttpResponse("hello the world!")


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            print("8888888")
            data = request.data;
            return Response("hello the world!")
        except BookInfo.DoesNotExist:
            return Response("hello the world!")

    def list(self, request, *args, **kwargs):
        print("1010101001")