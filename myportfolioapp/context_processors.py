from .models import *

def skillsdesc(request):
    skdesc=SkillsDesc.objects.all()
    return {'skdesc':skdesc}

def expdesc(request):
    edesc=ExpDesc.objects.all()
    return {'edesc':edesc}