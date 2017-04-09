from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from models import Business, Poi, Parking, Zone, Population


def index(request):
    context = {}
    return render(request, "index.html", context)


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
        try:
            zone=decode_zone(business_type)
        except:
            zone=business_type
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
    

def get_population_density(request):
    if request.method == 'GET':
        pop_type = request.GET.get('population_density_type')
        p = Population.objects.all()
        output = []
        
        if pop_type == 'age':
            age_range = request.GET.get('age_range')
            if age_range == 'age_under_5':
                output = [{'amount':x.age_under_5,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_5_9':
                output = [{'amount':x.age_5_9,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_10_14':
                output = [{'amount':x.age_10_14,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_15_19':
                output = [{'amount':x.age_15_19,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_20_24':
                output = [{'amount':x.age_20_24,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_25_34':
                output = [{'amount':x.age_25_34,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_35_44':
                output = [{'amount':x.age_35_44,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_45_54':
                output = [{'amount':x.age_45_54,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_55_59':
                output = [{'amount':x.age_55_59,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_60_64':
                output = [{'amount':x.age_60_64,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_65_74':
                output = [{'amount':x.age_65_74,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif age_range == 'age_75_84':
                output = [{'amount':x.age_75_84,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            else:
                output = [{'amount':x.age_over_85,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]             
        
        elif pop_type == 'gender':
            gender = request.GET.get('gender')
            if gender == 'males':
                output = [{'amount':x.males,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            else:
                output = [{'amount':x.females,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
        
        elif pop_type == 'education':
            education = request.GET.get('education')
            if education == 'edu_9th_grade':
                output = [{'amount':x.edu_9th_grade,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif education == 'edu_12th_grade':
                output = [{'amount':x.edu_12th_grade,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif education == 'edu_high_school':
                output = [{'amount':x.edu_high_school,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif education == 'edu_college':
                output = [{'amount':x.edu_college,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif education == 'edu_associate':
                output = [{'amount':x.edu_associate,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            elif education == 'edu_bachelors':
                output = [{'amount':x.edu_bachelors,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            else:
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.total_people,'locations':x.locations} for x in p]
            
        elif pop_type == 'income':
            income = request.GET.get('income')
            if income == 'incomes_below_10000':
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_below_10000,'total_households':x.total_households,'locations':x.locations} for x in p]
            elif income == 'incomes_10000_14999':
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_10000_14999,'total_households':x.total_households,'locations':x.locations} for x in p]
            elif income == 'incomes_15000_24999':
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_15000_24999,'total_households':x.total_households,'locations':x.locations} for x in p]
            elif income == 'incomes_25000_34999':
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_25000_34999,'total_households':x.total_households,'locations':x.locations} for x in p]
            elif income == 'incomes_35000_49999':
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_35000_49999,'total_households':x.total_households,'locations':x.locations} for x in p]
            elif income == 'incomes_75000_99999':
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_75000_99999,'total_households':x.total_households,'locations':x.locations} for x in p]
            elif income == 'incomes_100000_149999':
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_100000_149999,'total_households':x.total_households,'locations':x.locations} for x in p]
            elif income == 'incomes_150000_199999':
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_150000_199999,'total_households':x.total_households,'locations':x.locations} for x in p]
            else:
                output = [{'amount':x.edu_graduate,'zipcode':x.zipcode,'total_people':x.incomes_over_200000,'total_households':x.total_households,'locations':x.locations} for x in p]
           
                
            
        return JsonResponse({"output": output})
            
    else:
        return None  