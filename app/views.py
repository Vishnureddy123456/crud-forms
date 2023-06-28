from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is submitted')
    return render(request,'first.html')
