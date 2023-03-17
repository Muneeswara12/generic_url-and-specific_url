from django.shortcuts import render

# Create your views here.
def paper(request):
    return render(request,'paper.html')