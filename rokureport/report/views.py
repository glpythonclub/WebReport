# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def login(request):
    return render(request, 'report/login.html')

# Create your views here.
