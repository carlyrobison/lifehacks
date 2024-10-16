const riverMiles = 220;
const pxPerMile = 50 

function screenPos(riverMile) {
    return riverMile * pxPerMile
}

$(document).ready(function(){
    // jQuery methods go here...

    $("#rivermap").height(screenPos(riverMiles))
  
  });