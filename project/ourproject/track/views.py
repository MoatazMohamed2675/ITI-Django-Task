from django.shortcuts import redirect, render
from django.http import HttpResponse

from track.models import Track
# Create your views here.

def allTracks(request):
    context = {}
    context['tracks'] = Track.objects.all()
    return render(request,'track/list.html',context)

def getTrackById(request):
    return HttpResponse(f"<h1> hello from id track </h1>")

def updateTrack(request,id):
    # track=Track.objects.filter(id=id).update(status=True) if dont want to delete trainees in this track when deleted and set track to finished
    return redirect('alltracks')
    
def insertTrack(request):
    if request.method=='POST':
        track_name = request.POST.get('trname')
        Track.objects.create(name=track_name)
        return redirect('alltracks')
    return render(request,'track/insert.html')

def deleteTrack(request,id):
    Track.objects.filter(id=id).delete()
    # track=Track.objects.filter(id=id).update(status=False)
    # return redirect('alltracks') if dont want to delete trainees in this track when deleted
    return redirect('alltracks')
