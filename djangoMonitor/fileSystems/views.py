# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import os, platform, psutil

def fileSystems(request):
    def get_file_system():
        lists = os.popen('df -hT').read()
        return lists
    fileSystems = get_file_system()
    return render_to_response('filesystems.html', {
        'filesystems': fileSystems,
       })
