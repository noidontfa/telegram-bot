from django.http import HttpResponse
from django.shortcuts import render

from core.bot import TelegramBot


def index(request):
    return HttpResponse("Server is running")