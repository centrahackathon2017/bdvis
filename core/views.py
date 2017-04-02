from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from models import Business, Poi, Parking, Zone


def index(request):
    context = {}
    return render(request, "index.html", context)


def example_json_response(request):
    data = {"foo": "bar", "listdata": [1, 2, 3]}
    return JsonResponse(data)


def get_businesses(request):
   
    if request.method == 'GET':
        
        bus_type_list = request.GET.getlist('business_type')
        b=[]
        for t in bus_type_list:
            if t == 'all':
                b = Business.objects.all()
                break
            else:     
                b.extend(Business.objects.filter(category=t))

        output = [{'name':x.name,'phone':x.business_phone,'email':x.email,'location':x.location,'type':x.category,'start_date':x.start_date,'physical_address':x.physical_address,'mailing_address':x.mailing_address} for x in b]
        return JsonResponse({"output": output})
    else:
        return None
        

def get_facilities(request):
   
    if request.method == 'GET':

        facility_type = request.GET.getlist('facility_type')
        
        fac=[]
        for t in facility_type:
            fac.extend(Poi.objects.filter(category=t))

        
        output = [{'name':x.name,'location':x.location,'type':x.category} for x in fac]
        return JsonResponse({"output": output})
    else:
        return None  
