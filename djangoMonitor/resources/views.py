from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import os

def resources(request):
    def cpu_usage():
        usage = os.popen("ps aux|awk 'NR > 0 { s +=$3 }; END {print s}'").read()
        return usage
    def mem_usage():
        usage = os.popen("ps aux|awk 'NR > 0 { s +=$4 }; END {print s}'").read()
        return usage
    def top():
        top = os.popen('top -n 1 -b').read()
        return top
    cpu_usage = cpu_usage()
    mem_usage = mem_usage()
    top = top()
    return render_to_response('resources.html', {
        'cpu_load': cpu_usage,
        'mem_usage': mem_usage,
        'top': top,
        })
