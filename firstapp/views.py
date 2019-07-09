from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from firstapp.models import *
from django.http import HttpResponse

def home_view(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def signup(request):
    if request.method=='POST':
          context={}
          context['capitalist']=CapitalistInfoForm()
          context['startup']=OrganisationInfoForm()

          if 'investor' in request.POST:
              print("hii")
              context['capitalist'] = CapitalistInfoForm(request.POST)
              if context['capitalist'].is_valid():
                    context['capitalist'].save(commit=True);


          elif 'org' in request.POST:
             context['startup'] =OrganisationInfoForm(request.POST)
             if context['startup'].is_valid():
                  context['startup'].save(commit=True)

          return render(request,'signup.html',context)
    else:

        context={}
        context['capitalist']=CapitalistInfoForm()
        context['startup']=OrganisationInfoForm()
        return render(request, 'signup.html',context)

'''def startupRegistration(request):
    if request.method=='POST':
        form = OrganisationInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True);
            return render(request, 'org_registration.html', {'form': form})
    else:
        form=OrganisationInfoForm()
        return render(request, 'org_registration.html', {'form': form})

def capitalistRegistration(request):
    if request.method == 'POST':
        form = CapitalistInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'vc_registration.html', {'form': form})
    else:
        form = CapitalistInfoForm()
        return render(request, 'vc_registration.html', {'form': form})
'''
def login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            choice=form.cleaned_data['choice']
            if choice=='1':
                curuser=OrganisationInfo.objects.all().filter(username=username,password=password)
                if curuser:
                    list_id = curuser.values('id');
                    return redirect('first_app:after_login',choice=choice,id=list_id[0]['id'])
                else:
                    messages.error(request, 'Incorrect Username or Password')
            else:
                curuser = CapitalistInfo.objects.all().filter(username=username, password=password)
                if curuser:
                    list_id = curuser.values('id')
                    return redirect('first_app:after_login', id=list_id[0]['id'], choice=choice )
                else:
                    messages.error(request, 'Incorrect Username or Password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def after_login(request,choice,id):
    print("After login")
    if choice==1:
        return render(request,'after_org_login.html',{'id':id})
    else:
        return render(request,'after_vc_login.html',{'id':id})
