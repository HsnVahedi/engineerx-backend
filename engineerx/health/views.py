import os
from django.http import HttpResponse, Http404

def check_readiness(request):
    if os.path.exists('done'):
        return HttpResponse("OK")
    else:
        raise Http404()