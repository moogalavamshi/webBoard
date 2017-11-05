from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Board


def home(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'home.html', context)


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
