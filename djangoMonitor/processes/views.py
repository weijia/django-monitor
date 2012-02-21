# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import os, platform, psutil

def processes():
   return render_to_response('processes.html', {

       })
