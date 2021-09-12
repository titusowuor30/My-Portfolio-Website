from .models import *

def skillsdesc(request):
    skdesc=SkillsDesc.objects.all()
    return {'skdesc':skdesc}

def expdesc(request):
    edesc=ExpDesc.objects.all()
    return {'edesc':edesc}


def setName(request):
    name=About.objects.values_list('business_name')[0]
    return {'name':name}     

def setTel(request):
    tel=About.objects.values_list('phone')[0]
    return {'tel':tel}        

def setEmail(request):
    email=About.objects.values_list('business_email')[0]
    return {'email':email}    

def setAddres(request):
    adres=About.objects.values_list('business_address')[0]
    return {'adres':adres}

def setBg(request):
    bg=About.objects.values_list('background_image')[0]
    return {'bg':bg}           