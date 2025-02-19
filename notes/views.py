from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Notes

# Create your views here.

def home(request):
    context={}
    if request.method == 'POST':
        note=request.POST.get('note','')
        if note:
            Notes.objects.create(note=note)
            return redirect('home')
        else:
            context['error'] = 'Error : The field should not be empty'
    context['operation'] = '+ Add Note'
    notes=Notes.objects.all().order_by('-id')
    context['notes'] = notes
    
    return render(request,'home.html',context)

def update_note(request,id):
    context={}
    try:
        note=Notes.objects.get(id=id)
        context['note']=note
    except:
        context['error'] = '404 : Note not found !!'
    if request.method == 'POST':
        note_=request.POST.get('note','')
        note.note=note_
        note.save()
        return redirect('home')
    context['operation'] = 'Update'
    return render(request,'update.html',context)

def delete_note(request,id):
    try:
        note=Notes.objects.get(id=id)
        note.delete()
        return redirect('home')
    except:
        return HttpResponse('404 : Note not found !!')
