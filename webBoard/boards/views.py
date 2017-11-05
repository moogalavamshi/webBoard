from django.shortcuts import render
from django.http import HttpResponse

from .models import Board


def home(request):
    html = ''
    for board in Board.objects.all():
        html += '<br>' + board.name

    return HttpResponse(html)
