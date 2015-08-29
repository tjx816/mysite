# -*- coding: utf-8 -*-
from django.http import httpResponse

def first_page(request):
	return HttpResponse("<p>世界好</p>")