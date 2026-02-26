from multiprocessing import context
from signal import alarm
from ssl import AlertDescription
from django.shortcuts import render, redirect
from app import form
from app.form import TodoAppForm
from app.models import Todoapp


# Create your views here.
def LandingPage(request):

    todo = Todoapp.objects.all()
    context={
        "alltodo" : todo
    }


    return render(request, 'LandingPage.html' , context)

def AddTask(request):

    form = TodoAppForm()

    if request.method == 'POST':
        form = TodoAppForm(request.POST)
        if form.is_valid:
           form.save()
        return redirect('landingPageurl')



    context ={
        'myform': form
    }


    
    return render(request, 'addTask.html', context)

def EditTask(request, pk):
    todo =Todoapp.objects.get(id=pk)


    form = TodoAppForm()

    if request.method == 'POST':
        print('\n\n')
        print('method == post')
        print(request.POST)
        print('\n\n')
        form = TodoAppForm(request.POST, instance=todo)
            
        if form.is_valid:
            form.save()
            
            return redirect('landingPageurl')



    context ={
            'myform': form,
            'myTodo' : todo
        }




    return render(request, 'editTask.html',context)



def DeleteTask(request, pk):
    todo =Todoapp.objects.get(id=pk)

    todo.delete()
    return redirect('landingPageurl')


def PendTask(request):
    allPending =Todoapp.objects.filter(statue='pending')

    context ={
        'pendingTodo' : allPending
    }
    # mytodo  = Todoapp.objects.values_list('statue')
    # pending = TodoAppForm.get_template('pending.html')

    


    return render(request, 'pendingPage.html',context)
#   return HttpResponse(template.render(context, request))



    
def CompleteTask(request):
    allcomplete = Todoapp.objects.filter(statue='completed')

    context ={
        'completedTodo' : allcomplete
    }

    return render(request, 'completePage.html', context)

'''
person

name
complexion
gender
'''