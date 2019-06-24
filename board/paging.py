from math import ceil

from django.test import TestCase

# Create your tests here.
def paging(board, totalcount, currentpage):
    listsize = 5
    pagesize = 5

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
    endpage = (beginpage - 1) + listsize if (nextpage > 0) else pagecount
    start = (currentpage - 1) * pagesize

    forloop = [i for i in range(beginpage, (beginpage + listsize))]
    forindex = totalcount - (currentpage - 1) * listsize

    return {
        'boardlist': board[start:start + pagesize],
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

