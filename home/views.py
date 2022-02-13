from fileinput import filename
from django.shortcuts import render,redirect, get_object_or_404
from .forms import filesform
from .models import files
import mimetypes
import os
from django.http.response import HttpResponse

def home(request):
    if request.method == 'POST':
        form = filesform(request.POST, request.FILES)
        x = form.save()
        k = str(x.pk)
        return redirect('link/'+k)
    x = files.objects.all().count()
    return render(request,'home/index.html',{'forms':filesform,'x':x})


def link(request,upk):
    obj = get_object_or_404(files,pk = upk)
    form = filesform(instance=obj)
    values = files.objects.filter(pk = upk)
    x = files.objects.all().count()
    return render(request,'home/link.html',{'forms':form,'values':values,'x':x})
    