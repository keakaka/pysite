from django.http import HttpResponseRedirect
from django.shortcuts import render
from math import ceil
from board.models import Board
# Create your views here.

listsize = 5
pagesize = 5


def list(request, currentpage=0):
    try:
        currentpage = int(request.GET['currentpage'])
    except Exception as e:
        currentpage = 1
    totalcount = len(Board.objects.all())
    pagecount = ceil(totalcount / listsize)
    blockcount = pagecount // pagesize
    currentblock = ceil(currentpage / pagesize)
    if currentpage > pagecount:
        currentpage = pagecount
        currentblock = ceil(currentpage / pagesize)

    if currentpage < 1:
        currentpage = 1
        currentblock = 1

    beginpage = 1 if currentblock == 0 else (currentblock - 1) * pagesize + 1
    prevpage = (currentblock - 1) * pagesize if (currentblock > 1) else 0
    nextpage = currentblock * pagesize + 1 if (currentblock < blockcount) else 0
    endpage = (beginpage -1) + listsize if (nextpage > 0) else pagecount

    start = (currentpage - 1) * pagesize
    board = Board.objects.all().order_by('-regdate')[start:start + pagesize]
    forloop = [i for i in range(beginpage, (beginpage + listsize))]
    forindex = totalcount - (currentpage - 1) * listsize

    data = {
        'boardlist': board,
        'totalcount': totalcount,
        'listsize': listsize,
        'currentpage': currentpage,
        'beginpage': beginpage,
        'endpage': endpage,
        'prevpage': prevpage,
        'nextpage': nextpage,
        'forloop': forloop,
        'forindex': forindex
    }

    return render(request, 'board/list.html', data)


def writeform(request):
    return render(request, 'board/write.html')


def write(request):
    board = Board()

    board.title = request.POST['title']
    board.content = request.POST['content']
    board.user_id = request.POST['id']

    board.save()
    return HttpResponseRedirect('/board')


def delete(request):
    board = Board.objects.filter(id=request.GET['id'])
    board.status = 'N'
    board.save()

    return HttpResponseRedirect('/board')


def view(request):
    board = Board.objects.filter(id=request.GET['no'])
    data = {
        'board': board
    }
    return render(request, 'board/view.html', data)

