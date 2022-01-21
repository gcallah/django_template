import urllib.request
import re
import random

from django.http import request, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
from bs4 import BeautifulSoup as bs
from decimal import Decimal

from .models import Question


site_hdr = "Django Template"


def landing_page(request: request) -> object:
    try:
        modules = ["Blog post 1", "Blog post 2", "Blog post 3"]
        message_content = "Hello Lucia!"
        return render(
            request,
            "landing_page.html",
            {"modules": modules, "header": site_hdr, "message": message_content},
        )
    except Exception:
        message_content = "Database Not Connected"
        return render(
            request,
            "landing_page.html",
            {"header": site_hdr, "message": message_content},
        )
