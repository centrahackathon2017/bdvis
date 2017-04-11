

var mapOptions = {
  zoom: 11,
  center: {lat: 29.6508888, lng: -82.3242248},
  streetViewControl: false,
  mapTypeControl: false
}
var markerBusiness = []
var map = new google.maps.Map(document.getElementById('map'), mapOptions);


var dataBusiness = []
var indexBusiness = []
var nodeBusiness = []

function getLatLng(input){
      console.log(input)
      var data = input.split(',')
      data[0] = data[0].replace('[','')
      data[1] = data[1].replace(']','')
      return {lat:parseFloat(data[0]),lng:parseFloat(data[1])}
}

function getLat(input){
      var data = input.split(',')
      data[0] = data[0].replace('[','')
      data[1] = data[1].replace(']','')
      return parseFloat(data[0])
}

function getLng(input){
      var data = input.split(',')
      data[0] = data[0].replace('[','')
      data[1] = data[1].replace(']','')
      return parseFloat(data[1])
}

var cinemas = [];
var banks = [];
var pharmacies = [];
var churches = [];
var schools = [];
var fitnesses = [];
var nightlifes = [];
var groceries = [];
var restaurants = [];
var cinemaCnt=0, bankCnt=0, pharmacyCnt = 0, churchCnt = 0, schoolCnt=0, fitnessCnt=0, nightlifeCnt=0, groceryCnt=0, restaurantCnt=0;

function queryBusinessData(name){
    $.ajax({
        url: '/api/get_new_businesses',
        type: 'get',
        data: {business_type:name},
        cache: false,
        dataType: "json",
        success:  function(result){

        if(result.output.length>0){
            dataBusiness.push(result);

            var info;
            var markerData;

            for(var i=0;i<result.output.length;i++){

              var location = {lat : parseFloat(result.output[i].latitude), lng: parseFloat(result.output[i].longitude)}
              var cat = result.output[i].category;

              markerData = { company_name : result.output[i].company_name ,
                  category: result.output[i].category, fid : result.output[i].fid, address : result.output[i].address, city : result.output[i].city, state : result.output[i].state, zipcode : result.output[i].zipcode , 
                  latitude : result.output[i].latitude, longitude : result.output[i].longitude, industry_description : result.output[i].industry_description, 
                  indu_emp : result.output[i].indu_emp, serv_emp : result.output[i].serv_emp, comm_emp : result.output[i].comm_emp ,  estemp : result.output[i].estemp, totalpop : result.output[i].totalpop, 
                  households : result.output[i].households, male: result.output[i].male, female : result.output[i].female, white : result.output[i].white ,black : result.output[i].black, ameri_es :result.output[i].ameri_es,
                  asian : result.output[i].asian, hawn_pi: result.output[i].hawn_pi, other : result.output[i].other, mult_race : result.output[i].mult_race, hispanic : result.output[i].hispanic, white_nh : result.output[i].white_nh,
                  average_household_size : result.output[i].average_household_size, age_below_18 : result.output[i].age_below_18, age_18_40 : result.output[i].age_18_40, age_40_65 : result.output[i].age_40_65,
                  age_65_plus : result.output[i].age_65_plus, age_median : result.output[i].age_median, tran_total : result.output[i].tran_total,tran_car : result.output[i].tran_car, tran_moto : result.output[i].tran_moto,
                  tran_bike : result.output[i].tran_bike,tran_pub : result.output[i].tran_pub, tran_walk : result.output[i].tran_walk, tran_other : result.output[i].tran_other, tran_home : result.output[i].tran_home,
                  currently_student : result.output[i].currently_student, currently_not_student : result.output[i].currently_not_student, less_10k : result.output[i].less_10k, i10k_14k : result.output[i].i10k_14k,
                  i15k_19k : result.output[i].i15k_19k, i20k_24k : result.output[i].i20k_24k, i25k_29k : result.output[i].i25k_29k, i30k_34k : result.output[i].i30k_34k, i35k_39k : result.output[i].i35k_39k,
                  i40k_44k: result.output[i].i40k_44k, i45k_49k : result.output[i].i45k_49k, i50k_59k: result.output[i].i50k_59k, i60k_74k : result.output[i].i60k_74k, i75k_99k : result.output[i].i75k_99k, 
                  i100k_124k : result.output[i].i100k_124k, i125k_149k : result.output[i].i125k_149k, i150k_199k : result.output[i].i150k_199k, i200kmore : result.output[i].i200kmore, 
                  median_household_income : result.output[i].median_household_income, percent_bachelor_degree : result.output[i].percent_bachelor_degree, percent_poverty: result.output[i].percent_poverty

              };

              if(cat=='cinema'){
                  image = "../static/img/movie.png";

                  cinemas[cinemaCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(cinemas[cinemaCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(cinemas[cinemaCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(cinemas[cinemaCnt], 'click', function() {
                      showDetail(this.data);
                  });

                  cinemaCnt++;
              }else if(cat=='bank'){
                  image = "../static/img/bank.png";
                  banks[bankCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(banks[bankCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(banks[bankCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(banks[bankCnt], 'click', function() {
                      showDetail(this.data);
                  });

                  bankCnt++;
              }else if(cat=='pharmacy'){
                  image = "../static/img/pharmacy.png";
                  pharmacies[pharmacyCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(pharmacies[pharmacyCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(pharmacies[pharmacyCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(pharmacies[pharmacyCnt], 'click', function() {
                      showDetail(this.data);
                  });
                  pharmacyCnt++;
              }else if(cat=='church'){
                  image = "../static/img/church.png";
                  churches[churchCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(churches[churchCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(churches[churchCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(churches[churchCnt], 'click', function() {
                      showDetail(this.data);
                  });
                  churchCnt++;
              }else if(cat=='school'){
                  image = "../static/img/school.png";
                  schools[schoolCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(schools[schoolCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(schools[schoolCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(schools[schoolCnt], 'click', function() {
                      showDetail(this.data);
                  });
                  schoolCnt++;
              }else if(cat=='fitness'){
                  image = "../static/img/fitness.png";
                  fitnesses[fitnessCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(fitnesses[fitnessCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(fitnesses[fitnessCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(fitnesses[fitnessCnt], 'click', function() {
                      showDetail(this.data);
                  });
                  fitnessCnt++;
              }else if(cat=='nightlife'){
                  image = "../static/img/beer.png";
                  nightlifes[nightlifeCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(nightlifes[nightlifeCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(nightlifes[nightlifeCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(nightlifes[nightlifeCnt], 'click', function() {
                      showDetail(this.data);
                  });
                  nightlifeCnt++;
              }else if(cat== 'grocery'){
                  image = "../static/img/shop.png";
                  
                  groceries[groceryCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(groceries[groceryCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(groceries[groceryCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(groceries[groceryCnt], 'click', function() {
                      showDetail(this.data);
                  });
                  groceryCnt++;
              }else if(cat=='restaurant'){
                  image = "../static/img/restaurant.png";
                  
                  restaurants[restaurantCnt] = new google.maps.Marker({
                    position: location,
                    map: map,
                    icon: image,
                    info: new google.maps.InfoWindow({
                        content: result.output[i].company_name }),
                    data: markerData
                  });


                  google.maps.event.addListener(restaurants[restaurantCnt], 'mouseover', function() {
                      this.info.open(map,this);
                  });

                  google.maps.event.addListener(restaurants[restaurantCnt], 'mouseout', function() {
                      this.info.close();
                  });    

                  google.maps.event.addListener(restaurants[restaurantCnt], 'click', function() {
                      showDetail(this.data);
                  });
                  restaurantCnt++;
              }

            }
        }  

        },
        error:function(xhr,status){
            console.log('query error'+status);
        }
    });
}

function onAgeChange(event){
    queryAge(event.value)
}


function queryAge(age){
  console.log(age)
    $.ajax({
        url: 'http://127.0.0.1:8000/api/get_population_density',
        type: 'get',
        data: {population_density_type:'age',age_range:age},
        cache: false,
        dataType: "json",
        success:  function(result){

        console.log(result)
        if(result.output.length>0){

            for(var i=0;i<result.output.length;i++){
               console.log(result.output[i].locations)
            };
        }  
        },
        error:function(xhr,status){
            console.log('query error'+status);
        }
    });
}

function onMaleClick(){
  console.log('gender')
}




function closeChips(id){
  console.log(id)
  $('#'+id).remove()
  if(id=='bank'){
    for(var i=0;i<bankCnt;i++){
      banks[i].setMap(null);
      banks[i] = null;
    }
    banks = [];
    bankCnt = 0;
  }else if(id=='church'){
    for(var i=0;i<churchCnt;i++){
      churches[i].setMap(null);
      churches[i] = null;
    }
    churches = [];
    churchCnt = 0;
  }else if(id=='cinema'){
    for(var i=0;i<cinemaCnt;i++){
      cinemas[i].setMap(null);
      cinemas[i] = null;
    }
    cinemas = [];
    cinemaCnt = 0;
  }else if(id=='school'){
    for(var i=0;i<schoolCnt;i++){
      schools[i].setMap(null);
      schools[i] = null;
    }
    schools = [];
    schoolCnt = 0;
  }else if(id=='fitness'){
    for(var i=0;i<fitnessCnt;i++){
      fitnesses[i].setMap(null);
      fitnesses[i] = null;
    }
    fitnesses = [];
    fitnessCnt = 0;
  }else if(id=='grocery'){
    for(var i=0;i<groceryCnt;i++){
      groceries[i].setMap(null);
      groceries[i] = null;
    }
    groceries = [];
    groceryCnt = 0;
  }else if(id=='nightlife'){
    for(var i=0;i<nightlifeCnt;i++){
      nightlifes[i].setMap(null);
      nightlifes[i] = null;
    }
    nightlifes = [];
    nightlifeCnt = 0;
  }else if(id=='pharmacy'){
    for(var i=0;i<pharmacyCnt;i++){
      pharmacies[i].setMap(null);
      pharmacies[i] = null;
    }
    pharmacies = [];
    pharmacyCnt = 0;
  }else if(id=='restaurant'){
    for(var i=0;i<restaurantCnt;i++){
      restaurants[i].setMap(null);
      restaurants[i] = null;
    }
    restaurants = [];
    restaurantCnt = 0;
  }else if(id=='ALL'){


      for(var i=0;i<bankCnt;i++){
        banks[i].setMap(null);
        banks[i] = null;
      }
      banks = [];
      bankCnt = 0;
    
      for(var i=0;i<churchCnt;i++){
        churches[i].setMap(null);
        churches[i] = null;
      }
      churches = [];
      churchCnt = 0;
    
      for(var i=0;i<cinemaCnt;i++){
        cinemas[i].setMap(null);
        cinemas[i] = null;
      }
      cinemas = [];
      cinemaCnt = 0;
    
      for(var i=0;i<schoolCnt;i++){
        schools[i].setMap(null);
        schools[i] = null;
      }
      schools = [];
      schoolCnt = 0;
    
      for(var i=0;i<fitnessCnt;i++){
        fitnesses[i].setMap(null);
        fitnesses[i] = null;
      }
      fitnesses = [];
      fitnessCnt = 0;
    
      for(var i=0;i<groceryCnt;i++){
        groceries[i].setMap(null);
        groceries[i] = null;
      }
      groceries = [];
      groceryCnt = 0;
    
      for(var i=0;i<nightlifeCnt;i++){
        nightlifes[i].setMap(null);
        nightlifes[i] = null;
      }
      nightlifes = [];
      nightlifeCnt = 0;
    
      for(var i=0;i<pharmacyCnt;i++){
        pharmacies[i].setMap(null);
        pharmacies[i] = null;
      }
      pharmacies = [];
      pharmacyCnt = 0;

      for(var i=0;i<restaurantCnt;i++){
        restaurants[i].setMap(null);
        restaurants[i] = null;
      }
      restaurants = [];
      restaurantCnt = 0;

  } //end if ALL

}

var all = false;
var bid = 0;
function onBusinessChange(event){
  indexBusiness.push(event.value)
  if(event.value=='ALL'){
    queryBusinessData('all');
    all = true
    $('.wraplist').html('');
    $('.wraplist').prepend('<div id='+event.value+' class="chip"><span class="chiptext">ALL</span><img class="chipicon" src="../static/img/ic_clear_white.svg" onClick="closeChips(\''+event.value+'\')"/></div>');
  }else{
    queryBusinessData(event.value);
    if(all==true){
       $('.wraplist').html('');
       all = false;
    }
    $('.wraplist').prepend('<div id='+event.value+' class="chip"><span class="chiptext">'+event.value+'</span><img class="chipicon" src="../static/img/ic_clear_white.svg" onClick="closeChips(\''+event.value+'\')"/></div>');
    bid++;
  }
}


/*--------------------------------------
RIGHT PANEL
---------------------------------------*/
// TEST ONLY
// queryDetail('pharmacy');

// function queryDetail(type){
//     $.ajax({
//         url: '/api/get_new_businesses',
//         type: 'get',
//         data: {business_type:type},
//         cache: false,
//         dataType: "json",
//         success:  function(result){
//             showDetail(result.output[0])
//         },
//         error:function(xhr,status){
//             console.log('QUERY DETAIL ERROR: '+status);
//         }
//     });
// }

var employmentChart = null
var genderChart = null
var ageChart = null
var educationChart = null
var transportChart = null
var peopleChart = null
var revenueChart = null

function showDetail(data){
    $('.detaillabel').hide()
    $('.detaildata').show()
    $('.rightheader').text(data.company_name)
    $('#address').text(data.address)
    $('#citydetail').text(data.city)
    $('#state').text(data.state)
    $('#zipcode').text(data.zipcode)
    $('#latitude').text(data.latitude)
    $('#longitude').text(data.longitude)
    console.log(data)

    if(genderChart!=null){
        employmentChart.destroy()
        genderChart.destroy()
        ageChart.destroy()
        educationChart.destroy()
        transportChart.destroy()
        peopleChart.destroy()
        revenueChart.destroy()
    }
    

    employmentChart = new Chart($('#employmentChart'),{
        type: 'pie',
        data: {
          labels: [
            "Industrial",
            "Service related",
            "Commercial"
          ],
          datasets: [
            {
                data: [data.indu_emp, data.serv_emp, data.comm_emp],
                backgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56"
                ],
                hoverBackgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56"
                ]
          }]
        },
        options:{
            responsive: true,
            legend: {
                labels:{
                  boxWidth: 30,
                  usePointStyle: true
                }
            }
        }
    });

    genderChart = new Chart($('#genderChart'),{
        type: 'pie',
        data: {
          labels: [
            "Male",
            "Female"
          ],
          datasets: [
            {
                data: [data.male, data.female],
                backgroundColor: [
                    "#36A2EB",
                    "#FFCE56"
                ],
                hoverBackgroundColor: [
                    "#36A2EB",
                    "#FFCE56"
                ]
          }]
        },
        options:{
            responsive: true,
            legend: {
                labels:{
                  boxWidth: 30,
                  usePointStyle: true
                }
            }
        }
    });

    ageChart = new Chart($('#ageChart'),{
        type: 'pie',
        data: {
          labels: [
            "Below 18",
            "18-40",
            "40-65",
            "65 Plus"
          ],
          datasets: [
            {
                data: [data.age_below_18, data.age_18_40, data.age_40_65, data.age_65_plus],
                backgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56"
                ],
                hoverBackgroundColor: [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56"
                ]
          }]
        },
        options:{
            responsive: true,
            legend: {
                labels:{
                  boxWidth: 30,
                  usePointStyle: true
                }
            }
        }
    });

    educationChart = new Chart($('#educationChart'), {
        data: {
          datasets: [{
            data: [
                data.percent_bachelor_degree,
                data.percent_poverty
            ],
            backgroundColor: [
                "#FF6384",
                "#4BC0C0"
            ],
            label: 'My dataset' // for legend
            }],
            labels: [
                "Bachelor degree",
                "Poverty"
            ]
        },
        type: 'polarArea',
        options:{
            responsive: true,
            legend: {
                labels:{
                  boxWidth: 30,
                  usePointStyle: true
                }
            }
        }
    });

    transportChart = new Chart($('#transportChart'),{
        type: 'bar',
        data: {
            labels: ["Car", "Moto", "Bike", "Pub", "Walk", "Home", "Other"],
            datasets: [{
                data: [data.tran_car, data.tran_moto, data.tran_bike, data.tran_pub, data.tran_walk, data.tran_home, data.tran_other],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(86, 244, 66, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(86, 244, 66, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
            responsive: true,
            legend: {
                display: false
            }
        }
    });

    peopleChart = new Chart($('#peopleChart'),{
        type: 'bar',
        data: {
            labels: ["White", "Black", "Ameri es", "Asian", "Hawn pi", "Mult race", "Hispanic", "White nh", "Other"],
            datasets: [{
                data: [data.white, data.black, data.ameri_es, data.asian, data.hawn_pi, data.mult_race, data.hispanic, data.white_nh, data.other],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(86, 244, 66, 0.2)',
                    'rgba(244, 176, 66, 0.2)',
                    'rgba(65, 91, 244, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(86, 244, 66, 1)',
                    'rgba(244, 176, 66, 1)',
                    'rgba(65, 91, 244, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
            responsive: true,
            legend: {
                display: false
            }
        }
    });

    revenueChart = new Chart($('#revenueChart'),{
        type: 'bar',
        data: {
            labels: ["10k-14k","15k-19k","20k-24k", "25k-29k", "30k-34k", "35k-39k", "40k-44k", "45k-49k", "50k-59k", "60k-74k", "75k-99k", "100k-124k", "125k-149k","150k-199k","200k Plus"],
            datasets: [{
                data: [data.i10k_14k, data.i15k_19k, data.i20k_24k, data.i25k_29k, data.i30k_34k, data.i35k_39k,data.i40k_44k,data.i45k_49k,data.i50k_59k,data.i60k_i74k,data.i75k_99k,data.i100k_124k,data.i125k_149k,data.i150k_199k,data.i200kmore],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(86, 244, 66, 0.2)',
                    'rgba(244, 176, 66, 0.2)',
                    'rgba(65, 91, 244, 0.2)',
                    'rgba(244, 65, 88, 0.2)',
                    'rgba(187, 65, 244, 0.2)',
                    'rgba(244, 176, 66, 0.2)',
                    'rgba(65, 91, 244, 0.2)',
                    'rgba(244, 65, 88, 0.2)',
                    'rgba(187, 65, 244, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(86, 244, 66, 1)',
                    'rgba(244, 176, 66, 1)',
                    'rgba(65, 91, 244, 1)',
                    'rgba(244, 65, 88, 1)',
                    'rgba(187, 65, 244, 1)',
                    'rgba(244, 176, 66, 1)',
                    'rgba(65, 91, 244, 1)',
                    'rgba(244, 65, 88, 1)',
                    'rgba(187, 65, 244, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
            responsive: true,
            legend: {
                display: false
            }
        }
    });
}


// ------------------------------------

function onEnterCircle(node){
  $(node).css("color","#80cbc4")

}
function onLeaveCircle(node){
  $(node).css("color","#D7D5D5")
}

$('.btn--public').mouseenter(function(){
  onEnterCircle('.text--public');
  $('.icon--public').attr('src','../static/img/public_park_white.png');
}).mouseleave(function(){
  onLeaveCircle('.text--public')
  $('.icon--public').attr('src','../static/img/public_park.png');
})

$('.btn--fire').mouseenter(function(){
  onEnterCircle('.text--fire');
  $('.icon--fire').attr('src','../static/img/fire_station_white.png');
}).mouseleave(function(){
  onLeaveCircle('.text--fire')
  $('.icon--fire').attr('src','../static/img/fire_station.png');
})

$('.btn--bus').mouseenter(function(){
  onEnterCircle('.text--bus');
  $('.icon--bus').attr('src','../static/img/bus_stop_white.png');
}).mouseleave(function(){
  onLeaveCircle('.text--bus')
  $('.icon--bus').attr('src','../static/img/bus_stop.png');
})

$('.btn--parkings').mouseenter(function(){
  onEnterCircle('.text--parkings');
  $('.icon--parkings').attr('src','../static/img/parkings_white.png');
}).mouseleave(function(){
  onLeaveCircle('.text--parkings')
  $('.icon--parkings').attr('src','../static/img/parkings.png');
})

$('.btn--male').mouseenter(function(){
  onEnterCircle('.text--male');
  $('.icon--male').attr('src','../static/img/male_white.png');
}).mouseleave(function(){
  onLeaveCircle('.text--male')
  $('.icon--male').attr('src','../static/img/male.png');
})

$('.btn--female').mouseenter(function(){
  onEnterCircle('.text--female');
  $('.icon--female').attr('src','../static/img/female_white.png');
}).mouseleave(function(){
  onLeaveCircle('.text--female')
  $('.icon--female').attr('src','../static/img/female.png');
})

$('.btn--both').mouseenter(function(){
  onEnterCircle('.text--both');
  $('.icon--both').attr('src','../static/img/both_white.png');
}).mouseleave(function(){
  onLeaveCircle('.text--both')
  $('.icon--both').attr('src','../static/img/both.png');
})

let list = [0,0,0,0,0]
$('.gender').click(function(){
  if(list[2] == 0){
    $('.gendericon').attr('src','../static/img/ic_remove.svg');
    $('.genderspan').show();
    list[2] = 1

    $('.gendersicon').attr('src','../static/img/ic_add.svg');
    $('.gendersspan').hide();
    list[1] = 0

     $('.ageicon').attr('src','../static/img/ic_add.svg');
    $('.agespan').hide();
    list[0] = 0

    $('.educationicon').attr('src','../static/img/ic_add.svg');
    $('.educationspan').hide();
    list[3] = 0

     $('.nationalicon').attr('src','../static/img/ic_add.svg');
    $('.nationalspan').hide();
    list[4] = 0
  }else{
    $('.gendericon').attr('src','../static/img/ic_add.svg');
    $('.genderspan').hide();
    list[2] = 0
  }
})

$('.age').click(function(){
  if(list[0] == 0){
    $('.ageicon').attr('src','../static/img/ic_remove.svg');
    $('.agespan').show();
    list[0] = 1

    $('.gendersicon').attr('src','../static/img/ic_add.svg');
    $('.gendersspan').hide();
    list[1] = 0

    $('.gendericon').attr('src','../static/img/ic_add.svg');
    $('.genderspan').hide();
    list[2] = 0

    $('.educationicon').attr('src','../static/img/ic_add.svg');
    $('.educationspan').hide();
    list[3] = 0

     $('.nationalicon').attr('src','../static/img/ic_add.svg');
    $('.nationalspan').hide();
    list[4] = 0
  }else{
    $('.ageicon').attr('src','../static/img/ic_add.svg');
    $('.agespan').hide();
    list[0] = 0
  }
})

$('.genders').click(function(){
  if(list[1] == 0){
    $('.gendersicon').attr('src','../static/img/ic_remove.svg');
    $('.gendersspan').show();
    list[1] = 1

    $('.gendericon').attr('src','../static/img/ic_add.svg');
    $('.genderspan').hide();
    list[2] = 0

    $('.ageicon').attr('src','../static/img/ic_add.svg');
    $('.agespan').hide();
    list[0] = 0

     $('.educationicon').attr('src','../static/img/ic_add.svg');
    $('.educationspan').hide();
    list[3] = 0

     $('.nationalicon').attr('src','../static/img/ic_add.svg');
    $('.nationalspan').hide();
    list[4] = 0
  }else{
    $('.gendersicon').attr('src','../static/img/ic_add.svg');
    $('.gendersspan').hide();
    list[1] = 0
  }
})

$('.education').click(function(){
  if(list[3] == 0){
    $('.educationicon').attr('src','../static/img/ic_remove.svg');
    $('.educationspan').show();
    list[3] = 1

    $('.gendersicon').attr('src','../static/img/ic_add.svg');
    $('.gendersspan').hide();
    list[1] = 0

    $('.gendericon').attr('src','../static/img/ic_add.svg');
    $('.genderspan').hide();
    list[2] = 0

    $('.ageicon').attr('src','../static/img/ic_add.svg');
    $('.agespan').hide();
    list[0] = 0

    $('.nationalicon').attr('src','../static/img/ic_add.svg');
    $('.nationalspan').hide();
    list[4] = 0
  }else{
    $('.educationicon').attr('src','../static/img/ic_add.svg');
    $('.educationspan').hide();
    list[3] = 0
  }
})

$('.national').click(function(){
  if(list[4] == 0){
    $('.nationalicon').attr('src','../static/img/ic_remove.svg');
    $('.nationalspan').show();
    list[4] = 1

    $('.educationicon').attr('src','../static/img/ic_add.svg');
    $('.educationspan').hide();
    list[3] = 0

    $('.gendersicon').attr('src','../static/img/ic_add.svg');
    $('.gendersspan').hide();
    list[1] = 0

    $('.gendericon').attr('src','../static/img/ic_add.svg');
    $('.genderspan').hide();
    list[2] = 0

    $('.ageicon').attr('src','../static/img/ic_add.svg');
    $('.agespan').hide();
    list[0] = 0
  }else{
    $('.nationalicon').attr('src','../static/img/ic_add.svg');
    $('.nationalspan').hide();
    list[4] = 0
  }
})


//---Bam
var parkMarker=[];
var publicParkAmount = 0;
var parkLat = [];
var parkLng = [];
var parkType = [];
var parkName = [];
var showParkStatus = false;

$('.btn--public').click(function(){

    if(showParkStatus==false){
        $.ajax({
            url: '/api/get_facilities?facility_type=PARK',
            type: 'GET',
            datatype: 'json',
            crossDomain: true ,
            success:  function(result){

                publicParkAmount=result.output.length-1;

                //get resource descriptions
                for(var i=0; i<publicParkAmount; i++){
                    //main information
                    parkType[i] = result.output[i].type;
                    parkName[i] = result.output[i].name;
                    loc = JSON.parse(result.output[i].location);
                    parkLat[i] = loc[1];
                    parkLng[i] = loc[0];
                }
                showParkMarker();
                showParkStatus = true;
            },
            error:function(xhr,status){
                console.log(status);
            }
          }); 

      }else{
        
        hideParkMarker();
        showParkStatus = false;
      }
    
});



function showParkMarker(){
  var image = '../static/img/park.png';
    for(var i=0;i<publicParkAmount;i++){
      myLatLng = {lat: parkLat[i], lng: parkLng[i]};
      parkMarker[i] = new google.maps.Marker({
            position: myLatLng,
            map: map,
            icon: image
          });
    }
    
}

function hideParkMarker(){
    for(var i=0;i<publicParkAmount;i++){
      parkMarker[i].setMap(null);
      parkMarker[i] = null;

    }
    publicParkAmount=0;
}

var fireMarker=[];
var fireAmount = 0;
var fireLat = [];
var fireLng = [];
var fireType = [];
var fireName = [];
var showFireStatus = false;


$('.btn--fire').click(function(){

    if(showFireStatus==false){
        $.ajax({
            url: '/api/get_facilities?facility_type=FIRE STATION',
            type: 'GET',
            datatype: 'json',
            crossDomain: true ,
            success:  function(result){

                fireAmount=result.output.length-1;

                //get resource descriptions
                for(var i=0; i<fireAmount; i++){
                    //main information
                    fireType[i] = result.output[i].type;
                    fireName[i] = result.output[i].name;
                    loc = JSON.parse(result.output[i].location);
                    fireLat[i] = loc[1];
                    fireLng[i] = loc[0];
                }
                showFireMarker();
                showFireStatus = true;
            },
            error:function(xhr,status){
                console.log(status);
            }
          }); 

      }else{
        
        hideFireMarker();
        showFireStatus = false;
      }
    
});



function showFireMarker(){
  var image = '../static/img/firestation.png';
    for(var i=0;i<fireAmount;i++){
      myLatLng = {lat: fireLat[i], lng: fireLng[i]};
      fireMarker[i] = new google.maps.Marker({
            position: myLatLng,
            map: map,
            icon: image
          });
    }
    
}

function hideFireMarker(){
    for(var i=0;i<fireAmount;i++){
      fireMarker[i].setMap(null);
      fireMarker[i] = null;

    }
    fireAmount=0;
}


var busMarker=[];
var busAmount = 0;
var busLat = [];
var busLng = [];
var busType = [];
var busName = [];
var showBusStatus = false;


$('.btn--bus').click(function(){

    if(showBusStatus==false){
        $.ajax({
            url: '/api/get_facilities?facility_type=BUS STOP',
            type: 'GET',
            datatype: 'json',
            crossDomain: true ,
            success:  function(result){

                busAmount=result.output.length-1;

                //get resource descriptions
                for(var i=0; i<busAmount; i++){
                    //main information
                    busType[i] = result.output[i].type;
                    busName[i] = result.output[i].name;
                    loc = JSON.parse(result.output[i].location);
                    busLat[i] = loc[1];
                    busLng[i] = loc[0];
                }
                showBusMarker();
                showBusStatus = true;
            },
            error:function(xhr,status){
                console.log(status);
            }
          }); 

      }else{
        
        hideBusMarker();
        showBusStatus = false;
      }
    
});



function showBusMarker(){
  var image = '../static/img/busstop.png';
    for(var i=0;i<busAmount;i++){
      myLatLng = {lat: busLat[i], lng: busLng[i]};
      busMarker[i] = new google.maps.Marker({
            position: myLatLng,
            map: map,
            icon: image
          });
    }
    map.setZoom(13);
    
}

function hideBusMarker(){
    for(var i=0;i<busAmount;i++){
      busMarker[i].setMap(null);
      busMarker[i] = null;

    }
    busAmount=0;
}



var parkingAmount = 0;
var showParkingAreaStatus = false;
var p_type = [];
var parkingArea = [];

$('.btn--parkings').click(function(){

    if(showParkingAreaStatus==false){
        $.ajax({
            url: '/api/get_parkings',
            type: 'GET',
            datatype: 'json',
            crossDomain: true ,
            success:  function(result){

                parkingAmount=result.output.length-1;
                console.log('amount '+parkingAmount);

                for(var i=0;i<parkingAmount;i++){

                    p_type[i] = result.output[i].type;
                    console.log(typeof(p_type[i]));
                    if(p_type[i]=="LOT"){
                      //polygon
                      var areaCoor = [];

                      pathObj = JSON.parse(result.output[i].location)
                      console.log(pathObj[i][0]);
                      for(var i=0;i<pathObj.length;i++){
                          areaCoor.push({lat: parseFloat(pathObj[i][1]), lng: parseFloat(pathObj[i][0])});
                      
                    }
                      console.log('coordinate :');
                      console.log(areaCoor);
                      parkingArea[i] = new google.maps.Polygon({
                        paths: areaCoor,
                        strokeColor: '#FF0000',
                        strokeOpacity: 0.8,
                        strokeWeight: 2,
                        fillColor: '#FF0000',
                        fillOpacity: 0.35,
                        map : map
                      });
                      
                    }else{
                      //line
                    }
                }
                
                //showParkingArea();
                showParkingAreaStatus = true;
            },
            error:function(xhr,status){
                console.log(status);
            }
          }); 

      }else{
        
        //hideParkingArea();
        showParkingAreaStatus = false;
      }
    
});


var parkingAmount = 0;
var showParkingAreaStatus = false;
var p_type = [];


function showZone(event){
  console.log(event.value)

    if(showParkingAreaStatus==false){
        $.ajax({
            url: '/api/get_zoning?business_type='+event.value,
            type: 'GET',
            datatype: 'json',
            crossDomain: true ,
            success:  function(result){

                    var areaCoor = [

            {lng: -82.325779601, lat: 28.4697827309},
            {lng: -82.0245493745, lat: 28.6702959247},
            {lng: -82.1245493745, lat: 29.4702959247},
            {lng: -82.2245493745, lat: 29.6702959247},
            {lng: -82.325779601, lat: 28.4697827309}];

                      console.log(areaCoor);
                      parkingArea = new google.maps.Polygon({
                        paths: areaCoor,
                        strokeColor: '#FF0000',
                        strokeOpacity: 0.8,
                        strokeWeight: 2,
                        fillColor: '#FF0000',
                        fillOpacity: 0.35,
                        map : map});
              
                showParkingAreaStatus = true;
            },
            error:function(xhr,status){
                console.log(status);
            }
          }); 

      }else{
        
        //hideParkingArea();
        showParkingAreaStatus = false;
      }
    
}

var cityLayer  = null;

function showCityBorder(event){
    console.log('city : ' +event.checked);
    if(event.checked){
        cityLayer = new google.maps.KmlLayer({
          url: 'http://centrahack01.acis.ufl.edu/static/kml/CITY3.kmz',
          //url: 'http://lima-vc-1.sdsc.optiputer.net/project/CITY3.kmz',
          map: map
        });
    }else{
        cityLayer.setMap(null);
        cityLayer = null;
    }

}

var neighbourhoodLayer  = null;

function showNeighbourhoodBorder(event){
    console.log('Neighbourhood : ' +event.checked);
    if(event.checked){
        neighbourhoodLayer = new google.maps.KmlLayer({
          url: 'http://centrahack01.acis.ufl.edu/static/kml/NEIGHBORHOODS3.kmz',
          //url: 'http://lima-vc-1.sdsc.optiputer.net/project/NEIGHBORHOODS3.kmz',
          map: map
        });
    }else{
        neighbourhoodLayer.setMap(null);
        neighbourhoodLayer = null;
    }
}
