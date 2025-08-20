from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import Djangoform,Registrationform,Fileregistration
from sampleproject import settings
from django.core.mail import send_mail
from .models import Registration,Employee,Employeepoints,Trainer,testing,Post
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
# Create your views here.
# def first(request):
#     return HttpResponse("<h5>welcome</h5>")
from django.db.models import Avg,Max

def first(request):
    a="django"
    average_likes = Post.objects.aggregate(avg_likes=Avg('likes'))
    return HttpResponse(average_likes)
def show(request):
    return HttpResponse("<i>welcome to django</i>")

def display(request):
    a="django"
    b=[1,2,3,4]
    c=""
    return render(request,"first.html",{'data':a,'view':b,"first":c})

def parent(request):
    return render(request,'parent.html')

def child(request):
    return render(request,"child.html")

def cssstyle(request):
    return render(request,"style.html")

from django.template import loader

def view(request):
    a="djangooooooo"
    x=loader.get_template("oneone.html")
    return HttpResponse(x.render({'d':a}))

def djangoforms(request):
    x=Djangoform
    return render(request,"djangoform.html",{'data':x})

def regform(request):
    if request.method=="POST":
        s=Registrationform(request.POST)
        if s.is_valid():
            s.save()
        return HttpResponse("worked")
    else:
        x=Registrationform
        return render(request,"reg.html",{'view':x})
    
def regview(request):
    average = Registration.objects.aggregate(avg_name=Avg('age'))
    print(average)
    max = Registration.objects.aggregate(maxage=Max('age'))
    print(max)

    a=Registration.objects.all()
    return render(request,'regview.html',{'view':a})

def regdelete(request):
    d=Registration.objects.get(id=id)
    d.delete()
    return redirect(regview)

def regedit(request,id):
    print("its working")
    e=Registration.objects.get(id=id)
    return render(request,'regedit.html',{'edit':e})

def regupdate(request,id):
    e=Registration.objects.get(id=id)
    u=Registrationform(request.POST,instance=e)
    if u.is_valid():
        u.save()
        return redirect(regview)
    return render(request('regedit.html',{'edit':e}))

from sampleproject import settings
from django.core.mail import send_mail

def newmail(request):
    subject="django"
    msg="django is a python framework"
    to="keerthanaquest@gmail.com"
    result=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if result==1:
        m="success"
    else:
        m="failed"
    return HttpResponse(m)

def employees(request):
    if request.method=='POST':
        f=request.POST['firstname']
        l=request.POST['lastname']
        a=request.POST['age']
        e=request.POST['email']
        ph=request.POST['phone']
        u=request.POST['username']
        p=request.POST['password']
        # print(f,l,a,e,p,u,p)
        z=Employee.objects.create(firstname=f,lastname=l,age=a,email=e,phone=ph,username=u,password=p)
        z.save()
        return HttpResponse("worked")
    else:
        return render(request,"employee.html")


def view_emp(request):
    view=Employee.objects.all()
    return render(request,'view_emp.html',{'v':view})

def emp_delete(request,id):
    d=Employee.objects.get(id=id)
    d.delete()
    return HttpResponse("<script>alert('file is deleted');window.location.href='http://127.0.0.1:8000/view_emp';</script>")
    # return redirect(view_emp)

def emp_edit(request,id):
    e=Employee.objects.get(id=id)
    return render(request,'edit_em.html',{'edit':e})

def emp_update(request,id):
    if request.method=='POST':
        f=request.POST['firstname']
        l=request.POST['lastname']
        a=request.POST['age']
        e=request.POST['email']
        p=request.POST['phone']
        u=request.POST['username']
        password=request.POST['password']
        x=Employee.objects.get(id=id)
        x.firstname=f
        x.lastname=l
        x.age=a
        x.email=e
        x.phone=p
        x.username=u
        x.password=password
        x.save()
        return redirect(view_emp)

def regfile(request):
    if request.method=='POST':
        z=Fileregistration(request.POST,request.FILES)
        if z.is_valid():
            z.save()
        return HttpResponse("uploaded")
    else:
        x=Fileregistration
        return render(request,"file.html",{'data':x})


def emppoint(request):
    if request.method=='POST':
        eid=request.POST['empid']
        points=request.POST['points']
        x=Employeepoints.objects.create(points=points,empid_id=eid)
        x.save()
        return HttpResponse('success')
    else:
        x=Employee.objects.all()
        return render(request,'emppoint.html',{'data':x})

def setcookie(request):
    r=HttpResponse("COOKIE IS SET")
    r.set_cookie('django',"its a framework")
    return 

def getcookie(request):
    s=request.COOKIES['django']
    return HttpResponse(s)

def setsession(request):
    request.session['name']="ammu"
    return HttpResponse("session is set")

def getsession(request):
    x=request.session['name']
    return HttpResponse(x)

from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView

class TrainerCreate(CreateView):
    model=Trainer
    template_name='trainercreate.html'
    fields=['firstname','lastname','age','email','phone']
    success_url='/trainercreate/'

class TrainerList(ListView):
    model=Trainer
    template_name='trainerlist.html'
    context_object_name='e'

class TrainerDetail(DetailView):
    model=Trainer
    template_name='trainerdetail.html'
    context_object_name='e'

class TrainerUpdate(UpdateView):
    model=Trainer
    template_name='trainercreate.html'
    fields=['firstname','lastname','age','email','phone']
    success_url='/trainercreate/'

class TrainerDelete(DeleteView):
    model=Trainer
    template_name='trainerdelete.html'
    success_url='/trainercreate/'


def test1(request):
    if request.method=="POST":
        images=request.FILES['pic']
        x=testing.objects.create(image_lawn=images)
        x.save()
        return HttpResponse("saved")
    else:
        return render(request,'test.html')

def vtest1(request):
    view = testing.objects.all()
    return render(request,'details.html',{'views':view})