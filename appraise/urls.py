# -*- coding: utf-8 -*-
"""
Project: Appraise evaluation system
 Author: Christian Federmann <cfedermann@dfki.de>
"""
from django.conf.urls.defaults import patterns, include, handler404, \
  handler500
from django.contrib import admin
from django.views.generic.list_detail import object_list, object_detail

from appraise.settings import MEDIA_ROOT, DEBUG

admin.autodiscover()

urlpatterns = patterns('',
  (r'^appraise/$', 'appraise.views.frontpage'),
  (r'^appraise/login/$', 'appraise.views.login',
    {'template_name': 'login.html'}),
  (r'^appraise/logout/$', 'appraise.views.logout',
    {'next_page': '/appraise/'}),
  (r'^appraise/admin/', include(admin.site.urls)),

  (r'^appraise/evaluation/', 'appraise.evaluation.views.overview'),
  (r'^appraise/ranking-classification/(?P<task_id>[a-f0-9]{32})/',
    'appraise.evaluation.views.ranking'),
  (r'^appraise/post-editing/(?P<task_id>[a-f0-9]{32})/',
    'appraise.evaluation.views.editing'),
  (r'^appraise/quality-checking/(?P<task_id>[a-f0-9]{32})/',
    'appraise.evaluation.views.quality_checking'),
)

if DEBUG:
    urlpatterns += patterns('',
      (r'^appraise/site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    )