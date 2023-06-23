from django.shortcuts import render
from app.models import* 
from django.db.models.functions import Length

# Create your views here.
def display_topic(requsest):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(requsest,'display_topic.html',d)

def display_webpage(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(topic_name='cricket')
    webpages=Webpage.objects.exclude(topic_name='cricket')
    webpages=Webpage.objects.order_by('topic_name')
    webpages=Webpage.objects.order_by('-topic_name')
    webpages=Webpage.objects.order_by(Length('name'))
    webpages=Webpage.objects.order_by(Length('topic_name').desc())

    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    accessrecord=AccessRecord.objects.all()
    d={'accessrecord':accessrecord}
    return render(request,'display_accessrecord.html',d)

