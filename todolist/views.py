from django.shortcuts import render

tasks = []

# Create your views here.
def index(request):
    return render(request, "todolist/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "todolist/add.html")