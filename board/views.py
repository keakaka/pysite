from django.db.models import F, Max, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from math import ceil
from board.models import Board
# Create your views here.
from board.paging import paging


def list(request):
    currentpage = int(request.GET.get('currentpage', 1))
    keyword = request.POST.get('keyword', '')
    ordering = ['-groupno', 'orderno']
    board = Board.objects.filter(Q(title__contains=keyword) | Q(content__contains=keyword)).order_by(*ordering)

    return render(request, 'board/list.html', paging(board, len(board), currentpage))


def writeform(request):
    return render(request, 'board/write.html')


def write(request):
    board = Board()

    try:
        groupno = int(request.POST['groupno'])
        orderno = int(request.POST['orderno'])
        depth = int(request.POST['depth'])
        Board.objects.filter(groupno=groupno). \
            filter(orderno__gte=orderno + 1). \
            update(orderno=F('orderno') + 1)

        board.title = request.POST['title']
        board.content = request.POST['content']
        board.user_id = request.POST['user_id']
        board.groupno = groupno
        board.orderno = orderno + 1
        board.depth = depth + 1

    except Exception as e:
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.user_id = request.POST['user_id']
        board.groupno = groupno_max() + 1

    board.save()
    return HttpResponseRedirect('/board')


def groupno_max():
    value = Board.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno = 0 if value["max_groupno"] is None else value["max_groupno"]
    return max_groupno


def delete(request):
    board = Board.objects.get(id=request.GET['id'])
    board.status = 'N'
    board.save()

    return HttpResponseRedirect('/board')


def view(request):
    board = Board.objects.get(id=request.GET['id'])
    board.hit = board.hit+1
    board.save()
    data = {
        'board': board
    }
    return render(request, 'board/view.html', data)


def updateform(request):
    board = Board.objects.get(id=request.GET['id'])
    data = {
        'board': board
    }
    return render(request, 'board/updateform.html', data)


def update(request):
    id = request.POST['id']
    board = Board.objects.get(id=id)

    board.content = request.POST['content']
    board.title = request.POST['title']

    board.save()

    return HttpResponseRedirect(f'/board/view?id={id}')


def replyform(request):
    board = Board.objects.get(id=request.GET['id'])
    data = {
        'board': board
    }
    return render(request, 'board/replyform.html', data)

