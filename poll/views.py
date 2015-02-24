from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from poll.models import *
import json
import os
from backend import MultiRunCounter
cur_dir = os.path.dirname(os.path.abspath(__file__))

import datetime
import os
def sayhi(request):
    result = os.popen('dir').read().split('\n')
    return HttpResponse("Hello,this is my first django web!<br> %s %s" %('<br>'.join(result),datetime.datetime.now()))
def index(request):
    return render_to_response('index.html')
def servermgmt(request):
    groups = Group.objects.all()
    remote_user_list = PollUser.objects.get(user__username=request.user).remoteuser.all()
    return render_to_response('servermgmt.html',{'group_list':groups,'remote_user_list':remote_user_list,'user':request.user})

def runcmd(request):
    print request.POST
    track_mark = MultiRunCounter.AddNumber()
    user_input = request.POST['cmd']
    user_account = request.POST['SelectUser']
    SelectedIPs = []
    GroupList = Group.objects.all()
    for g_name in GroupList:
        if g_name.name in request.POST.keys():
            print "slected group:",g_name.name
            for selected_ip in IP.objects.filter(group__name = g_name.name):
                SelectedIPs.append(selected_ip.IP)
    #print ' '.join(set(SelectedIPs))
    # print request.POST.get('cmd')
    cmd = "python %s/backend/multiprocessing_runCMD2.py %s '%s' '%s' %s &" % (cur_dir,track_mark,'_'.join(set(SelectedIPs)),user_input,user_account)
    print("view.py cmd:",cmd)
    os.system(cmd)
    return HttpResponse(track_mark)

def getcmdresult(request):
    track_mark=request.GET['TrackMark']
    print track_mark
    cmd_result_record = OpsLog.objects.get(track_mark=track_mark)
    total_task = cmd_result_record.total_task
    success_num = cmd_result_record.success_num
    failed_num = cmd_result_record.failed_num
    cmd_feedback = OpsLogTemp.objects.filter(track_mark=track_mark).values('event_log','ip','result')
    #print cmd_feedback

    def result():
        #result_list = []
        data_dic = {}
        for i in cmd_feedback:
            print i['ip']
            data_dic[i['ip']] = i
        print data_dic
        return data_dic
    return HttpResponse(json.dumps(result() ))

def get_ip_list(request):
    g_name = request.GET['Name']
    print(g_name)
    ip_list = IP.objects.filter(group__name=str(g_name)).values('hostname','IP','os')
    # ManytoMany Query
    print ip_list
    ip_dic = {}
    for i in ip_list:
        ip_dic[i['hostname']] = i
    print(ip_dic)
    return HttpResponse(json.dumps(ip_dic))
    # return HttpResponse(g_name)

def account_login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    print(username,password)
    if user is not None: #and user.is_active:
        #correct password and user is marked "active"
        auth.login(request,user)
        return HttpResponseRedirect("/servermgmt/")
    else:
        return render_to_response('index.html',{'login_err':"Wrong username or Passowrd!!"})
def logout(request):
    user = request.user
    auth.logout(request)
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/'>Re-login</a>" % user)

def handler404(request):
    response = render_to_response('404.html', {},context_instance=RequestContext(request))
    response.status_code = 404
    return response
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
def hour_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
def dynamic_temp(request,offset):
    if len(offset) == 0:
        offset = 0
    else:
        offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return render_to_response('index.html',{'get_time':dt})
def name_list(request):
    f = file("name_list.txt").readlines()
    name = [i.strip('\n') for i in f]
    name_dict = dict([i.strip().split() for i in f])
    print(name)
    print(name_dict)
    return render_to_response('dict.html',{"name_list":name,"name_dict":name_dict.items()})
