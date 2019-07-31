from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth
from .models import Account , Workrecode

def home(request):
    worklist = Account.objects.all()
    workrecode = Workrecode.objects.all()

    return render(request,'home.html',{'worklist':worklist, 'workrecode':workrecode})


def signup(request):
        account=Account()
        account.name=request.POST['name']
        account.code=request.POST['code']
        account.save()
        return redirect('home')


def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(request, username=username , password = password)
                if user is not None:
                        auth.login(request,user)
                        return redirect('home')
                else:
                        return redirect('home')
        else:
                return redirect('home')
        
def controll(request,account_id):
        account_detail = get_object_or_404(Account, pk = account_id)
        return render(request,'controll.html',{'work':account_detail})

def workOrnot(request,account_id):
        account = Account.objects.get(id=account_id)
        
        if request.method == 'POST':
                if account.code == request.POST['code']:
                        account.youwork = request.POST['youwork']
                        account.save()

                        workrecode = Workrecode()
                        workrecode.name = account.name
                        workrecode.youwork = account.youwork
                        workrecode.pub_date = timezone.datetime.now()
                        workrecode.save()

                        return redirect('home')
                else:
                        
                        return redirect('home')

        else:
                return redirect('home')
        
def delete(request, account_id):
        account = Account.objects.get(id=account_id)
        account.delete()
        return redirect('home')
