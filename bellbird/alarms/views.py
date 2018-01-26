# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib, urllib2
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from alarms.forms import AlarmForm
from alarms.models import Alarm
# Create your views here.

class IndexView(TemplateView):
    template_name = "alarms/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["alarm_form"] = AlarmForm()
        return context


class AlarmView(FormView):
    form_class = AlarmForm
    success_url = "/alarms/"

    def form_valid(self, form):
        alarm = form.save()
        post_data = [('alarm_id', alarm.pk)]
        # external API call
        result = urllib2.urlopen('http://handshake-bellbird.herokuapp.com/push', urllib.urlencode(post_data))
        # print(result.read())
        return super(AlarmView, self).form_valid(form)

class RecentAlarmsView(View):
    def get(self, request):
        return JsonResponse(serializers.serialize('json', Alarm.objects.order_by('-created_at', 'votes')[:10]), safe=False)


class AlarmsListView(ListView):
    model = Alarm


class UpvoteAlarmView(View):

    def post(self, request, *args, **kwargs):
        print(self.kwargs['pk'])
        alarm = Alarm.objects.get(pk=self.kwargs['pk'])
        alarm.votes += 1
        alarm.save()
        return JsonResponse({'status': 'success'}, safe=False)
