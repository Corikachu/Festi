# coding: utf8
from django.conf.urls import patterns, include, url
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import User, Event, Survey


@require_http_methods(['POST'])
@csrf_exempt
def user_new(request):
    u'새 유저 등록'
    raise NotImplemented


@require_http_methods(['PUT'])
@csrf_exempt
def user_update(request, user_uid):
    u'유저 정보 수정'
    print request.PUT
    user = get_object_or_404(User, uid=user_uid)
    raise NotImplemented


def events_list(request):
    u'이벤트 목록 조회'
    Event.objects.filter(is_public=True)
    raise NotImplemented


def event_detail(request, event_id):
    u'이벤트 내용 조회'
    event = get_object_or_404(Event, id=event_id)
    raise NotImplemented


@require_http_methods(['POST'])
@csrf_exempt
def survey_new(request, event_id):
    u'이벤트 신청'
    raise NotImplemented


@require_http_methods(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def survey_form(request, event_id, user_uid):
    u'이벤트 신청내용 조회/수정/삭제'
    survey = get_object_or_404(Survey, event__id=event_id, user__uid=user_uid)

    if request.method == 'GET':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass

    raise NotImplemented


urlpatterns = patterns('',
    url(r'^users/$', user_new, name='user_new'),
    url(r'^users/(?P<user_uid>\d+)/$', user_update, name='user_update'),
    url(r'^events/$', events_list, name='events_list'),
    url(r'^events/(?P<event_id>\d+)/$', event_detail, name='event_detail'),
    url(r'^events/(?P<event_id>\d+)/users/$', survey_new, name='survey_new'),
    url(r'^events/(?P<event_id>\d+)/users/(?P<user_uid>\d+)/$', survey_form, name='survey_form'),
)
