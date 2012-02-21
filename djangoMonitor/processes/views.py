# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import os, platform, psutil

def processes(request):
    def get_processes():
        lists = os.popen('ps axjf').read()
        return lists
    processes = get_processes()
    return render_to_response('processes.html', {
        'processes': processes, 
       })
