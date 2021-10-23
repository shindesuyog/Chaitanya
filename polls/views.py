from django.shortcuts import render,redirect
from .forms import Studentregistration
from .models import User
from django.http import HttpResponse


# Create your views here.
#this fucunctoin is use to add stu
def add_show(request):
    if request.method == 'POST':
        fm = Studentregistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            #fm.save()
            reg.save()
    else:
        fm = Studentregistration()
    stud=User.objects.all()
    return render(request,'polls/addshow.html',{'form':fm,'stu':stud})

def update_data(request, id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        fm= Studentregistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm= Studentregistration(instance=pi)
    
    return render(request,'polls/update.html',{'form':fm})
    


def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return redirect("/polls/std")
