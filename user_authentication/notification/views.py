from django.shortcuts import render
from models import Notification
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def show_unviewed_notifications(request):
    request.session['unread_notifications']=str(Notification.objects.filter(viewed=False,user=request.user).count())#nu e cod de calitate, incerc sa folosesc notifications cu swampdragon: https://github.com/wildfish/swampdragon-django-notifications-demo
    return render(request,'notification/notifications.html',{'notifications':Notification.objects.filter(viewed=False,user=request.user)})

@login_required
def view_notification(request,notification_id):
    notification=Notification.objects.get(id=notification_id)
    notification.viewed=True
    notification.save()
    messages.success(request,'A notification was marked as read')
    request.session['unread_notifications']=str(Notification.objects.filter(viewed=False,user=request.user).count())
    response=HttpResponseRedirect('/notifications/show_all_unviewed')
    #response.set_cookie( 'unread_notifications', str(Notification.objects.filter(viewed=False,user=request.user).count()) )
    return response