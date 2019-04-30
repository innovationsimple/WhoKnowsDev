# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def redirectToVue(request, *args, **kwargs):
    return render(request, 'vue.html')


def dynamic_files(request, ftype):
    if ftype == 'js':
        content_type = 'text/javascript'

    elif ftype == 'css':
        content_type = 'text/css'

    return render(request, 'dynamic.' + ftype, {}, content_type=content_type)
