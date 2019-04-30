# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, response


# Create your views here.
class TestViewSet(viewsets.ViewSet):
    def list(self, request, **kwargs):
        return response.Response({
            'msg': 'This is a test response from django api'
        })


class AppCategoryViewSet(viewsets.ViewSet):
    def list(self, request, **kwargs):
        return response.Response({
            'myapps': [
                {
                    'name': 'Test App',
                    'desc': 'This is a test app description',
                    'link': 'http://example.com',
                    'alert_text': '',
                    'is_public': True,
                    'has_login': False,
                    'link_target': '',
                    'sub_title': 'Sub Title Goes Here',
                    'show_image': False,
                    'logosrc': '',
                    'id': 1,
                    'new_tab': False,
                }
            ],
            'app_categories': [
                {
                    'name': 'Marketing & Selling',
                    'apps': [
                        {
                            'name': 'Test App',
                            'desc': 'This is a test app description',
                            'link': 'http://example.com',
                            'alert_text': '',
                            'is_public': True,
                            'has_login': False,
                            'link_target': '',
                            'sub_title': 'Sub Title Goes Here',
                            'show_image': False,
                            'logosrc': '',
                            'id': 1,
                            'new_tab': False,
                        }
                    ],
                }, {
                    'name': 'People & H.R.',
                    'apps': [
                        {
                            'name': 'Test App',
                            'desc': 'This is a test app description',
                            'link': 'http://example.com',
                            'alert_text': '',
                            'is_public': True,
                            'has_login': False,
                            'link_target': '',
                            'sub_title': 'Sub Title Goes Here',
                            'show_image': False,
                            'logosrc': '',
                            'id': 1,
                            'new_tab': False,
                        }
                    ],
                }, {
                    'name': 'Operations',
                    'apps': [
                        {
                            'name': 'Test App',
                            'desc': 'This is a test app description',
                            'link': 'http://example.com',
                            'alert_text': '',
                            'is_public': True,
                            'has_login': False,
                            'link_target': '',
                            'sub_title': 'Sub Title Goes Here',
                            'show_image': False,
                            'logosrc': '',
                            'id': 1,
                            'new_tab': False,
                        }
                    ],
                }, {
                    'name': 'Finance & Reporting',
                    'apps': [
                        {
                            'name': 'Test App',
                            'desc': 'This is a test app description',
                            'link': 'http://example.com',
                            'alert_text': '',
                            'is_public': True,
                            'has_login': False,
                            'link_target': '',
                            'sub_title': 'Sub Title Goes Here',
                            'show_image': False,
                            'logosrc': '',
                            'id': 1,
                            'new_tab': False,
                        }
                    ],
                }
            ],
        })
