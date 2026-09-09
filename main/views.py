from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Muhammad Zahran Affan",
        "npm": "2506586103",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information Systems student at Fasilkom UI, "
            "currently exploring different paths and figuring out where I fit best."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Muhammad Zahran Affan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)