from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Business, Poi, Parking, Zone, Population, NewBusiness
from utils.Calculate import predict

def index(request):
    context = {}
    return render(request, "index.html", context)

def get_business_prediction(request):
  if request.method == 'GET':
    lat = request.GET.getlist('lat')
    lng = request.GET.getlist('lng')
    success = predict(lat, lng)
    return JsonResponse({"output": success})
    # return JsonResponse({"output": 80})
  else:
    return None

def get_new_businesses(request):
    
    if request.method == 'GET':
        bus_type_list = request.GET.getlist('business_type')
        b=[]
        for t in bus_type_list:
            if t == 'all':
                b = NewBusiness.objects.all().order_by('category')
                break
            else:     
                b.extend(NewBusiness.objects.filter(category=t))

        output = [{'category': x.category, 'fid' : x.fid, 'company_name' : x.company_name, 'address' : x.address, 'city' : x.city,'state' : x.state, 'zipcode' : x.zipcode , 'latitude' : x.latitude, 'longitude' : x.longitude, 'industry_description' : x.industry_description, 'indu_emp' : x.indu_emp, 'serv_emp' : x.serv_emp, 'comm_emp' : x.comm_emp ,  'estemp' : x.estemp,'totalpop' : x.totalpop, 'households' : x.households,'male': x.male, 'female' : x.female, 'white' : x.white ,'black' : x.black,'ameri_es' :x.ameri_es,'asian' : x.asian, 'hawn_pi': x.hawn_pi, 'other' : x.other,'mult_race' : x.mult_race, 'hispanic' : x.hispanic, 'white_nh' : x.white_nh,'average_household_size' : x.average_household_size, 'age_below_18' : x.age_below_18, 'age_18_40' : x.age_18_40,'age_40_65' : x.age_40_65,'age_65_plus' : x.age_65_plus, 'age_median' : x.age_median,'tran_total' : x.tran_total,'tran_car' : x.tran_car, 'tran_moto' : x.tran_moto,'tran_bike' : x.tran_bike,'tran_pub' : x.tran_pub, 'tran_walk' : x.tran_walk, 'tran_other' : x.tran_other, 'tran_home' : x.tran_home,'currently_student' : x.currently_student, 'currently_not_student' : x.currently_not_student, 'less_10k' : x.less_10k, 'i10k_14k' : x.i10k_14k,'i15k_19k' : x.i15k_19k, 'i20k_24k': x.i20k_24k, 'i25k_29k' : x.i25k_29k, 'i30k_34k' : x.i30k_34k, 'i35k_39k' : x.i35k_39k,'i40k_44k': x.i40k_44k,'i45k_49k' : x.i45k_49k, 'i50k_59k' : x.i50k_59k, 'i60k_74k' : x.i60k_74k, 'i75k_99k' : x.i75k_99k, 'i100k_124k' : x.i100k_124k,'i125k_149k' : x.i125k_149k, 'i150k_199k' : x.i150k_199k, 'i200kmore' : x.i200kmore, 'median_household_income' : x.median_household_income,'percent_bachelor_degree' : x.percent_bachelor_degree, 'percent_poverty': x.percent_poverty} for x in b]
        return JsonResponse({"output": output})
    else:
        return None
        

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