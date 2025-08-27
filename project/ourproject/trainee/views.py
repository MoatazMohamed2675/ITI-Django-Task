from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Trainee
from track.models import Track
# Create your views here.
def allTrainee(request):
    context = {}
    context['trainees'] = Trainee.getalltrainees().order_by('id')
    return render(request,'trainee/list.html',context)

def getTraineeId(request):
    return HttpResponse(f"<h1> hello from id trainee </h1>")

def updateTrainee(request,id):
    trainee = Trainee.gettraineebyid(id)
    context={'trainee':trainee}
    context['tracks']=Track.getalltracks()
    if request.method=='POST':
        trainee.name = request.POST.get('trname')
        trainee.email = request.POST.get('tremail')
        trainee.trackid = Track.gettrackbyid(request.POST.get('trtrack'))
        if request.FILES.get('trimage'):
            trainee.image = request.FILES.get('trimage')
        trainee.save()  
        return redirect('alltrainee') 
    return render(request,'trainee/update.html',context)

def insertTrainee(request):
    context={}
    context['tracks']=Track.getalltracks()
    if request.method=='POST':
        Trainee.objects.create(name=request.POST['trname'],email=request.POST['tremail'],image=request.FILES['trimage'],trackid=Track.gettrackbyid(request.POST['trtrack']))
        return redirect('alltrainee')
    return render(request,'trainee/insert.html',context)

def deleteTrainee(request,id):
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('alltrainee')