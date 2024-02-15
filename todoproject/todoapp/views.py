from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import TodoListItem 
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 
# Create your views here.
def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x,completed = False)
    
    new_item.save()
    return HttpResponseRedirect('/todoapp/') 
def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 
def complete(request, i):
    z=TodoListItem.objects.get(id= i)
    z.completed= True
    z.save()
    return HttpResponseRedirect('/todoapp/')