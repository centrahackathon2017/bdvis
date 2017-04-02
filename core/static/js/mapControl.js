

var mapOptions = {
  zoom: 11,
  center: {lat: 29.6508888, lng: -82.3242248},
  streetViewControl: false,
  mapTypeControl: false
}
var map = new google.maps.Map(document.getElementById('map'), mapOptions);

function queryData(){
    $.ajax({
        url: 'https://vernity.com/HeartProTech_admin/get_doctor_chart_right.php',
        type: 'get',
        data: {HN:'7777777'},
        cache: false,
        dataType: "json",
        success:  function(result){
            console.log(result)
        },
        error:function(xhr,status){
            console.log('query error'+status);
        }
    });
}

function closeChips(){
  
}

var all = false
function onBusinessChange(event){
  if(event.value=='ALL'){
    all = true
    $('.wraplist').html('');
    $('.wraplist').prepend('<div class="chip"><span class="chiptext">ALL</span><img class="chipicon" src="../static/img/ic_clear_white.svg" onClick="closeChips(this)"/></div>');
  }else{
    if(all==true){
       $('.wraplist').html('');
       all = false;
    }
    $('.wraplist').prepend('<div id='+event.value+' class="chip"><span class="chiptext">'+event.value+'</span><img class="chipicon" src="../static/img/ic_clear_white.svg" /></div>');
  }
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
                console.log('amount'+parkingAmount);

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
                
                showParkingArea();
                showParkingAreaStatus = true;
            },
            error:function(xhr,status){
                console.log(status);
            }
          }); 

      }else{
        
        hideParkingArea();
        showParkingAreaStatus = false;
      }
    
});


