var url ="http://" + "localhost" + ":5000/"

var urlPuppies = url + 'api/puppies'
var urlOwner = url + 'api/owner'

var selectPuppy;

$(document).ready(function () {

  $.get(urlPuppies, function (data, status) {
    console.log("Data: " + data + "\nStatus: " + status);
    selectPuppy = document.getElementById('selectPuppy');
    puppies = (JSON.parse(data));
    console.log(puppies)
    for (var puppy of puppies){
      $('#puppies').append('<div class="card" style="min-width:500px; min-height:250px; margin:15px; background: #eee;">' +
        '<div class="card-body"><h5 class="card-title">' + puppy.name + '</h5>' +
         '<p class="card-text"><span style="font-weight:bolder">Description: </span><span style="margin-left: 10px;">' + puppy.description + '</p>' +
        '<p class="card-text"><span style="font-weight:bolder">TAG: </span><span style="margin-left: 10px;">' + puppy.tag + '</p>' +
        ' </div> </div></br></br>');
      if(selectPuppy != null)
        selectPuppy.options.add( new Option(puppy.Name, puppy.Tag) ) 
    }
  });

  $('#buttonAdopt').on('click', function() {
    location.href = "owner.html";
  })

   $('#buttonBackToPuppy').on('click', function() {
    location.href = "puppies.html";
  })

    $('#buttonBackToHome').on('click', function() {
    location.href = "index.html";
  })


   $('#buttonAddOwner').click(function() {
    var my_json = {
      'name': $('#name').val(),
      'description': $('#description').val(),
      'puppy_name': $('#puppy_name').val()
    };

    my_url = urlOwner + "?name=" + my_json['name'] + "&description=" + my_json['description'] + "&puppy_name=" + my_json['puppy_name']
    console.log(my_url)

    $.ajax({
      type: "POST",
      url: my_url,
      contentType: "application/json; charset=utf-8",
      dataType: "JSON",
      data: JSON.stringify(my_json),
      success: function(result){
       console.log(result)
       if(result.status == 200){
        location.href = "owner.html";
      }
    }
  })
  
    location.href = "puppies.html";
  });

});