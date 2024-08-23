from django.shortcuts import render ,redirect
# from .forms import ToForm
from.models import To_do,History
# Create your views here.
def index(request):
    # data = To_do.objects.all()
    # form = ToForm(request.POST)
    if request.method == 'POST':
        task = request.POST.get('task')
        desc = request.POST.get('desc')
        To_do.objects.create(new_task = task,desc = desc)
        return redirect('home')
    
    return render(request,'index.html')


def details(request):
    data = To_do.objects.all().order_by('-id')
    context = {
        'data':data
    }
    return render(request,'details.html',context)
def list(request,pk):
    list = To_do.objects.get(id=pk)
    if request.method == 'POST':
        list.new_task 
        list.desc
        History.objects.create(new_task = list.new_task,desc = list.desc)
        list.delete()
        return redirect('home')
        
    context = {
        'list':list
    }
    return render(request,'list.html',context)
def edit(request,pk):
    list = To_do.objects.get(id=pk)
    if request.method == 'POST':
        task = request.POST.get('task')
        desc = request.POST.get('desc')

        list.new_task = task
        list.desc = desc
        list.save()
        return redirect('details')
    context = {
        'elist':list
    }
    return render(request,'edit.html',context)

def history(request):
    data = History.objects.all()
    if request.method =='POST':
        data.delete()
        return redirect('history')
    context = {
        'data':data
    }
    return render(request,'history.html',context)