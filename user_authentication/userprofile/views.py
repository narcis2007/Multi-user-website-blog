from django.shortcuts import render
from forms import UserProfileForm
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

@login_required
def edit_profile(request):
    if request.method=='POST':
        form=UserProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/'+str(request.user.id)+'/')
        else:
            args={}
            args.update(csrf(request))
            args['form']=form
            return render(request,'userprofile/edit_profile.html',args)
    user=request.user
    profile=user.profile
    args={}
    args.update(csrf(request))
    args['form']=UserProfileForm(instance=profile)
    return render(request,'userprofile/edit_profile.html',args)

def profile(request,user_id):
    user=User.objects.get(id=user_id)
    args={}
    args['user']=user
    return render(request,'userprofile/profile.html',args)