from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import calendar
import datetime
import os
from .modules import main, timecardgenerator, mailer, shift_mailer
from . import models
from django.contrib.auth.decorators import login_required

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

now = datetime.datetime.now()
thismonth = now.month
nextmonth = thismonth + 1
# Create your views here.


@login_required
def index(request):
    return render(request, 'djsg/index.html', {'nextmonth': nextmonth})


@login_required
def sg(request):

    pubholys = {4: [30], 5: [3, 4, 5], 6: ['無し'], 7: [16],
                8: [11], 9: [17, 24], 10: [8], 11: [3, 23], 12: [24]}
    noWorkingDays = {4: 8, 5: 6, 6: 10, 7: 8,
                     8: 12, 9: 9, 10: 8, 11: 11, 12: 9}  # 休刊日のディクショナリ
    thisyear = now.year
    pycalendar = calendar.HTMLCalendar(0).formatmonth(
        thisyear, nextmonth, withyear=True)
    message1 = f"{nextmonth}月の祝日は{pubholys[nextmonth]}、休刊日は{noWorkingDays[nextmonth]}です"

    return render(
        request, 'djsg/sg.html',
        {'pycalendar': pycalendar, 'message1': message1})


@login_required
def result(request):

        workernamelist = []
        workertypelist = []
        workerdayofflist = []
        workerlist = {}

        names = request.POST.getlist("worker-name")
        for i in names:
            workernamelist.append(i)

        types = request.POST.getlist("worker-type")
        for i in types:
            workertypelist.append(i)

        for i in request.POST.getlist("worker-dayoff"):
            i = str(i)
            workerdayofflist.append(i)

        for i in range(len(workernamelist)):
            workersinfo = {}
            workersinfo["属性"] = workertypelist[i]
            workersinfo["休み希望"] = workerdayofflist[i]
            workerlist[workernamelist[i]] = workersinfo

        main.shiftgenerator(workerlist)
        try:
            mailaddres = models.Workers.objects.all()
        except:
            pass

        return render(request,
                      'djsg/result.html',
                      {"nextmonth": nextmonth,
                       "mailaddres": mailaddres})


@login_required
def shiftmailer(request):

    info = request.POST.get("sel_mail")
    sendaddres = models.Workers.objects.get(worker_name=info).mail
    shift_mailer.sendmail(nextmonth, sendaddres)

    return render(request, 'djsg/sent.html')


@login_required
def shift(request):

    sel_month = request.POST.get("sel_month")
    SHIFTPATH = os.path.join(BASE_DIR, f'djsg/media/djsg/shifts/{sel_month}')
    print(sel_month)
    with open(SHIFTPATH, 'rb') as fh:
        response = HttpResponse(
            fh.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f"filename={sel_month}"
        return response


@login_required
def tg(request):
    try:
        d = models.Workers.objects.all()

    except:
        pass

    shlist = os.listdir(os.path.join(BASE_DIR, f'djsg/media/djsg/shifts'))
    newlist = []
    
    for i in shlist:
        
        newlist.append(i[:2])
    
    return render(request, 'djsg/tg.html', {"shiftslist":newlist, "d":d})


@login_required
def shiftslist(request):
    shlist= os.listdir(os.path.join(
        BASE_DIR,
        f'djsg/media/djsg/shifts'))

    return render(request, 'djsg/shiftslist.html', {'shiftslist': shlist})

@login_required
def timecard(request):
    try:
        sel_month = request.POST.get('sel-month')
        
        name = request.POST.get('name')
        f_name = request.POST.get('f_name')
        wnum = request.POST.get('w_num')
        mail = request.POST.get('mail')
        
        if request.method == "POST":
            if 'b2' in request.POST:
                db = models.Workers()
                db.worker_name = name
                db.worker_fname = f_name
                db.w_num = wnum
                db.mail = mail
                db.save()

                

        timecardgenerator.tcgen(sel_month, name, f_name, wnum)
        mailer.sendmail(mail, sel_month, name)    

        return render(request, 'djsg/sent.html')

    except Exception as e:
        return render(request, 'djsg/500.html')


def ajax(request):
    import json
    if request.method == 'POST':
        sel_name= request.POST.get('sel_person')
        print(sel_name)

        d = models.Workers.objects.get(worker_name=sel_name)
        
        ret = {
        "name" : d.worker_name,
        "f_name" : d.worker_fname,
        "w_num"  : d.w_num,
        "mail" : d.mail}
        print(ret)
        return JsonResponse(ret)


def register(request):
    try:
        d = models.Workers.objects.all()
        
    except:
        pass

    return render(request, 'djsg/register.html', {"d":d})


