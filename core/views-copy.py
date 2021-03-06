from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from models import Business, Poi, Parking, Zone


def index(request):
    context = {}
    return render(request, "index.html", context)


def get_businesses(request):
   
    if request.method == 'GET':
        bus_type_list = request.GET.getlist('business_type')
        b=[]
        for t in bus_type_list:
            s=''
            if t == 'all':
                from django.db.models import Count, Avg
                b = Business.objects.all().values('category').annotate(b=Count(0))
                for x in b:
                    s+='<option value="'+str(x['category'])+'">'+str(x['category'])+'</option>'
                
                break
            else:     
                b.extend(Business.objects.filter(category=t))
        return HttpResponse(s)
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
        
        
def get_parkings(request):
   
    if request.method == 'GET':
        park = Parking.objects.all()
        output = [{'location':x.locations,'type':x.category} for x in park]
        return JsonResponse({"output": output})
    else:
        return None  
        
        
def get_zoning(request):
   
    if request.method == 'GET':
        business_type = request.GET.get('business_type')
        zone=decode_zone(business_type)
        b=[]
        for z in zone:
            b.extend(Zone.objects.filter(zone=z))
        output = [{'pin':x.pin,'mp_nzone1':x.mp_nzone1,'mp_nzone2':x.mp_nzone2,'zone_code':x.zone,'zone':encode_zone(x.zone),'locations':x.locations} for x in b]
        return JsonResponse({"output": output})
    else:
        return None  
        

def decode_zone(x):
    return {
        'Airport Facility':['AF'],
        'Agriculture':['AGR'],
        'Automotive-Oriented Business':['BA'],
        'Business Industrial':['BI'],
        'Tourist-Oriented Business':['BT'],
        'General Business District':['BUS'],
        'Central City District':['CCD'],
        'Conservation':['CON'],
        'Corporate Park':['CP'],
        'Educational Services':['ED'],
        'Limited Industrial':['I-1'],
        'General Industrial':['I-2'],
        'Medical Services':['MD'],
        'Mobile Home Residential':['MH'],
        'Mixed Use Low Intensity':['MU-1'],
        'Mixed Use Medium Intensity':['MU-2'],
        'General Office':['OF'],
        'Office Residential':['OR'],
        'Planned Development':['PD'],
        'Public Services and Operations':['PS'],
        'Residential Conservation':['RC'],
        'Residential High Density':['RH-1','RH-2'],
        'Single-Family/Multiple-Family Residential':['RMF-5'],
        'Multiple-Family Residential':['RMF-6','RMF-7','RMF-8'],
        'Residential Mixed Use':['RMU'],
        'Single-Family Residential':['RSF-1','RSF-2','RSF-3','RSF-4'],
        'Urban Mixed-Use':['UMU-1','UMU-2'],
        'Warehousing and Wholesaling':['W']
    }[x]
    
    
def encode_zone(x):
    return {
        'AF':'Airport Facility',
        'AGR':'Agriculture',
        'BA':'Automotive-Oriented Business',
        'BI':'Business Industrial',
        'BT':'Tourist-Oriented Business',
        'BUS':'General Business District',
        'CCD':'Central City District',
        'CON':'Conservation',
        'CP':'Corporate Park',
        'ED':'Educational Services',
        'I-1':'Limited Industrial',
        'I-2':'General Industrial',
        'MD':'Medical Services',
        'MH':'Mobile Home Residential',
        'MU-1':'Mixed Use Low Intensity',
        'MU-2':'Mixed Use Medium Intensity',
        'OF':'General Office',
        'OR':'Office Residential',
        'PD':'Planned Development',
        'PS':'Public Services and Operations',
        'RC':'Residential Conservation',
        'RH-1':'Residential High Density',
        'RH-2':'Residential High Density',
        'RMF-5':'Single-Family/Multiple-Family Residential',
        'RMF-6':'Multiple-Family Residential',
        'RMF-7':'Multiple-Family Residential',
        'RMF-8':'Multiple-Family Residential',
        'RMU':'Residential Mixed Use',
        'RSF-1':'Single-Family Residential',
        'RSF-2':'Single-Family Residential',
        'RSF-3':'Single-Family Residential',
        'RSF-4':'Single-Family Residential',
        'UMU-1':'Urban Mixed-Use',
        'UMU-2':'Urban Mixed-Use',
        'W':'Warehousing and Wholesaling'
    }[x]