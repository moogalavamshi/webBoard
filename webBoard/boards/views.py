from django.shortcuts import render
from django.http import HttpResponse

from .models import Board


def home(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'home.html', context)


def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})
