from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import os, platform, psutil

def systemInfo(request):
    def hostname():
        file_open = open('/proc/sys/kernel/hostname')
        try:
            hostname = file_open.read()
        finally:
            file_open.close()
        return hostname
    def os_type():
        file_open = open('/proc/sys/kernel/ostype')
        try:
            os_type = file_open.read()
        finally:
            file_open.close()
        return os_type
    def os_release():
        x = os.popen('lsb_release  -a')
        os_release = ''
        br = '<html><br></html>'
        for line in x.readlines():
            os_release ='\t' +  os_release + line
        x.close()
        return os_release
    def kernel_release():
        file_open = open('/proc/sys/kernel/osrelease')
        try:
            kernel_release = file_open.read()
        finally:
            file_open.close()
        return kernel_release
    def desktop_environment():
        file_open = os.popen('gnome-session --version')
        try:
            desktop_environment = file_open.read()
        finally:
            file_open.close()
        return desktop_environment
    def memory_size():
        file_open = os.popen('cat /proc/meminfo')
        try:
            lines = file_open.readlines()
        finally:
            file_open.close()
        mem = {}
        stat = {}
        for line in lines:
            if len(line) < 2: continue
            name = line.split(':')[0]
            var = line.split(':')[1].split()[0]
            mem[name] = long(var)
        memory_size = mem['MemTotal']
        return memory_size
    def cpu_info():
        file_open = os.popen('cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c')
        try:
            lines = file_open.read()
        finally:
            file_open.close()
        cpu_model_name = lines
        return cpu_model_name
    def disk_size():
        file_open = os.popen('/bin/bash /home/code/django-monitor/djangoMonitor/scripts/disk_total.sh')
        disk_size = file_open.read()
        disk_size = disk_size
        return disk_size
    hostname = hostname()
    os_type = os_type()
    os_release = os_release()
    kernel_release = kernel_release()
    desktop_environment = desktop_environment()
    memory_size = memory_size()
    cpu_model_name = cpu_info()
    disk_size = disk_size()
    return render_to_response('system.html', {
        'hostname': hostname,
        'os_type': os_type,
        'os_release': os_release,
        'kernel_release': kernel_release,
        'desktop_environment': desktop_environment,
        'memory_size': memory_size,
        'cpu_model_name': cpu_model_name,
        'disk_size': disk_size,
        })
