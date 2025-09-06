# main/views.py
from django.shortcuts import render

def show_main(request):
    context = {
        "app_name": "Garuda Store",
        "student_name": "ZIbeon Jonriano Wisnumoerti",
        "class_name": "PBP D"
    }
    return render(request, "main.html", context)
