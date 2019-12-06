from django.shortcuts import render


def new_view(request):
  context = {
  
  }
  return render (request, "index.html", context)
