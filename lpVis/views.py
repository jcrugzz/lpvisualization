from django.shortcuts import render_to_response, get_object_or_404
from lpVis.models import *

def index(request):
    latest_landing_pages = LandingPage.objects.all()
    return render_to_response('lpVis/index.html', 
                {'latest_landing_pages': latest_landing_pages })
