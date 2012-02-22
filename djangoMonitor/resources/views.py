from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import os, string, settings
from pylab import *


def resources(request):
    def graphics(cpu, ram, network):
        # create figure
        figwidth = 10.0    # inches
        figheight = 3.5   # inches
        figure(1, figsize=(figwidth, figheight))
        rcParams['font.size'] = 12.0
        rcParams['axes.titlesize'] = 16.0
        rcParams['xtick.labelsize'] = 12.0
        rcParams['legend.fontsize'] = 12.0
        explode=(0.05, 0.0)
        colors=('b','g')
        Ncols = 3
        plotheight = figwidth/Ncols
        H = plotheight/figheight
        W = 1.0 / Ncols
        margin = 0.1
        left = [W*margin, W*(1+margin), W*(2+margin)]
        bottom = H*margin
        width = W*(1-2*margin)
        height = H*(1-2*margin)

        # cpu utilization
        cpu_utilized = cpu
        free = 100.0 - cpu_utilized
        fracs = [cpu_utilized, free]
        axes([left[0], bottom, width, height])
        patches = pie(fracs, colors=colors, explode=explode, autopct='%1.f%%', shadow=True)
        title('CPU Throughput')
        legend((patches[0], patches[2]), ('Processing', 'Idle'), loc=(0,-.05))

        # RAM utilization
        ram_utilized = ram
        free = 100.0 - ram_utilized
        fracs = [ram_utilized, free]
        axes([left[1], bottom, width, height])
        patches = pie(fracs, colors=colors, explode=explode, autopct='%1.f%%', shadow=True)
        title('ROM Memory Usage')
        legend((patches[0], patches[2]), ('Used', 'Unused'), loc=(0,-.05))

        # NET utilization
        net_utilized = network
        free = 100.0 - net_utilized
        fracs = [net_utilized, free]
        axes([left[2], bottom, width, height])
        patches = pie(fracs, colors=colors, explode=explode, autopct='%1.f%%', shadow=True)
        title('NETWORK Usage')
        legend((patches[0], patches[2]), ('Used', 'Unused'), loc=(0,-.05))

        os.popen('rm static/utilization.png -rf')
        savefig(settings.ROOT_PATH + '/media/' + 'utilization')
        return 0
    def cpu_usage():
        usage = os.popen("ps aux|awk 'NR > 0 { s +=$3 }; END {print s}'").read().strip()
        return usage
    def mem_usage():
        usage = os.popen("ps aux|awk 'NR > 0 { s +=$4 }; END {print s}'").read().strip()
        return usage
    def top():
        top = os.popen('top -n 1 -b').read()
        return top
    def net_usage():
        net_usage = 50
        return net_usage
    cpu_usage = string.atof(cpu_usage())
    mem_usage = string.atof(mem_usage())
    net_usage = net_usage()
    top = top()
    graphics(cpu_usage, mem_usage, net_usage)
    return render_to_response('resources.html', {
        'cpu_load': cpu_usage,
        'mem_usage': mem_usage,
        'top': top,
        })
