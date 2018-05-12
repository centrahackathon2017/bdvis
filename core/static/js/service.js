var service = function () {};

/**
 * Get business prediction
 * @param {string} lat 
 * @param {string} lng 
 * @param {function} callback 
 */
service.prototype.getBusinessPrediction = function (lat, lng, callback) {
  $.ajax({
    url: '/api/get_business_prediction?lat=' + lat + '&lng=' + lng,
    type: 'GET',
    datatype: 'json',
    crossDomain: true,
    success:  function(result) {
      var data = result.output || null;
      callback(data);
    },
    error:function(xhr, status){
      callback(null);
    }
  });
}