from django.shortcuts import render
from app.models import* 
from django.db.models.functions import Length
from django.db.models import Q

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
    webpages=Webpage.objects.filter(name__startswith='d')
    webpages=Webpage.objects.filter(name__endswith='i')
    webpages=Webpage.objects.filter(name__contains='o')
    webpages=Webpage.objects.filter(name__in=['sachin','dhoni'])
    webpages=Webpage.objects.filter(Q(name='dhoni')|Q(url__startswith='https'))


    
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    accessrecord=AccessRecord.objects.all()


    accessrecord=AccessRecord.objects.filter(date='1995-01-18')
    accessrecord=AccessRecord.objects.filter(date__gt='1995-01-18')
    accessrecord=AccessRecord.objects.filter(date__lt='1995-01-18')
    accessrecord=AccessRecord.objects.filter(date__lte='1995-01-18')
    accessrecord=AccessRecord.objects.filter(date__gte='1995-01-18')
    accessrecord=AccessRecord.objects.filter(date__year='2002')
    accessrecord=AccessRecord.objects.filter(date__month='06')
    accessrecord=AccessRecord.objects.filter(date__year__gte='2002')
    accessrecord=AccessRecord.objects.filter(date__year__lte='2002')
    accessrecord=AccessRecord.objects.filter(date__day__gt='12')
    
    

    
    
    d={'accessrecord':accessrecord}
    return render(request,'display_accessrecord.html',d)



