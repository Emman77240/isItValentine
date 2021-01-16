import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "checkvalentine/index.html", {
        "valentinesday": now.month == 2 and now.day == 14
    })