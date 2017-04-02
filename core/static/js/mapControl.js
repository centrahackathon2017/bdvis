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

function getLatLng(input){
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

function queryBusinessData(name){
    $.ajax({
        url: 'http://127.0.0.1:8000/api/get_businesses',
        type: 'get',
        data: {business_type:name},
        cache: false,
        dataType: "json",
        success:  function(result){
          console.log(result)
        if(result.output.length>0){
            dataBusiness.push(result)

            for(var i=0;i<result.output.length;i++){
              var location = getLatLng(result.output[i].location)
              var marker = new google.maps.Marker({
                  position: location,
                  map: map
              });

              var info = new google.maps.InfoWindow({
                  content: '<section><div class="labellat"><div class="col1">Name: </div><div class="col2 name">'+result.output[i].name+'</div></div><div class="labellng"><div class="col1">Type: </div><div class="col2 type">'+result.output[i].type+'</div></div><div class="labellng"><div class="col1">Phone: </div><div class="col2 phone">'+result.output[i].phone+'</div></div><div class="labellng"><div class="col1">Address: </div><div class="col2 ">'+result.output[i].physical_address+'</div></div><div class="labellng"><div class="col1">Email: </div><div class="col2">'+result.output[i].email+'</div></div><div class="labellng"><div class="col1">Lat: </div><div class="col2">'+getLat(result.output[i].location)+'</div></div><div class="labellng"><div class="col1">Lng: </div><div class="col2">'+getLng(result.output[i].location)+'</div></div></section>'
              });
              marker.addListener('mouseover', function() {
                  info.open(map,this)
              });
              marker.addListener('mouseout', function() {
                  info.close()
              });

              markerBusiness.push(marker)
            }
        }  

        },
        error:function(xhr,status){
            console.log('query error'+status);
        }
    });
}


function queryAge(name){
    $.ajax({
        url: 'http://127.0.0.1:8000/api/get_businesses',
        type: 'get',
        data: {business_type:name},
        cache: false,
        dataType: "json",
        success:  function(result){
          console.log(result)
        if(result.output.length>0){
            dataBusiness.push(result)

            for(var i=0;i<result.output.length;i++){
              var location = getLatLng(result.output[i].location)
              var marker = new google.maps.Marker({
                  position: location,
                  map: map
              });

              var info = new google.maps.InfoWindow({
                  content: '<section><div class="labellat"><div class="col1">Name: </div><div class="col2 name">'+result.output[i].name+'</div></div><div class="labellng"><div class="col1">Type: </div><div class="col2 type">'+result.output[i].type+'</div></div><div class="labellng"><div class="col1">Phone: </div><div class="col2 phone">'+result.output[i].phone+'</div></div><div class="labellng"><div class="col1">Address: </div><div class="col2 ">'+result.output[i].physical_address+'</div></div><div class="labellng"><div class="col1">Email: </div><div class="col2">'+result.output[i].email+'</div></div><div class="labellng"><div class="col1">Lat: </div><div class="col2">'+getLat(result.output[i].location)+'</div></div><div class="labellng"><div class="col1">Lng: </div><div class="col2">'+getLng(result.output[i].location)+'</div></div></section>'
              });
              marker.addListener('mouseover', function() {
                  info.open(map,this)
              });
              marker.addListener('mouseout', function() {
                  info.close()
              });

              markerBusiness.push(marker)
            }
        }  

        },
        error:function(xhr,status){
            console.log('query error'+status);
        }
    });
}


function closeChips(event){
  $('#'+event).remove()
}

var all = false;
var bid = 0;
function onBusinessChange(event){
  indexBusiness.push(event.value)
  if(event.value=='ALL'){
    queryBusinessData('all');
    all = true
    $('.wraplist').html('');
    $('.wraplist').prepend('<div id='+bid+' class="chip"><span class="chiptext">ALL</span><img class="chipicon" src="../static/img/ic_clear_white.svg" onClick="closeChips('+bid+')"/></div>');
  }else{
    queryBusinessData(event.value);
    if(all==true){
       $('.wraplist').html('');
       all = false;
    }
    $('.wraplist').prepend('<div id='+bid+' class="chip"><span class="chiptext">'+event.value+'</span><img class="chipicon" src="../static/img/ic_clear_white.svg" onClick="closeChips('+bid+')"/></div>');
    bid++;
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