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