# Create your views here.
from django.http import Http404, HttpResponse

def systemInfo(requet):
    html = "<html><title>System Information</title><body><h2>systemInfo</h2></body></html>"
    return HttpResponse(html)

def processes(requet):
    html = "<html><title>Process</title><body><h2>Process</h2></body></html>"
    return HttpResponse(html)

def resources(requet):
    html = "<html><title>Process</title><body><h2>Resources</h2></body></html>"
    return HttpResponse(html)
