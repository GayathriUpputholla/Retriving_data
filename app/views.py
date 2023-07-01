from django.shortcuts import render
from app.models import* 
from django.db.models.functions import Length
from django.db.models import Q
from django.http import HttpResponse

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
    webpages=Webpage.objects.all()


    
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


def update_webpage(request):
    # Webpage.objects.filter(name='sachin').update(url='https://schin.in')
    #Webpage.objects.filter(topic_name='cricket').update(url='https://india.in')
    #Webpage.objects.filter(name='msd dhoni').update(url='https://msd.in')
    #Webpage.objects.filter(name='ramesh').update(url='BCCI CRICKET')
    # Webpage.objects.filter(name='raj').update(url='https://raj.in')
    #Webpage.objects.update_or_create(name='raj',defaults={'url':'http://raj.com'})


    CTO=Topic.objects.get(topic_name='cricket')
    #Webpage.objects.update_or_create(name='raj',defaults={'topic_name':CTO})
    #Webpage.objects.update_or_create(name='raj',defaults={'topic_name':CTO,'url':'http://raj.com'})




    
     







    
    d={'webpages':Webpage}
    return render(request,'diplay_webpage.html',d)



def delete_webpage(request):
    d={'webpages':Webpage}
    Webpage.objects.filter(name='raj').delete()
    return render(request,'diplay_webpage.html',d)

    

    


