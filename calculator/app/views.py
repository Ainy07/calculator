from django.http import HttpResponse
from django.shortcuts import render


def app(request):
    return render(request,'index.html',{'name':'programmers point'})
     
def cal(request):
    a=request.GET['n1']
    b=request.GET['n2']
    ch=request.GET['ch']
    a=int(a)
    b=int(b)
    c=0
    if ch=="Add":
        c=a+b
    elif ch=="Sub":
        c=a-b
    elif ch=="Mul":
        c=a*b
    elif ch=="Div":
        try:
            c=a/b
        except ZeroDivisionError:
            c="unable to devide by zero"               
    return render(request,'result.html',{'result':c})

def calculator(request):
    val=request.POST['val']
    return render(request,'result.html',{'result':eval(val)})