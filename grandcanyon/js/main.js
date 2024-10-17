const riverMiles = 220;
const pxPerMile = 50;
const padding = 20;  // pixels
var headerSize = 0;  // pixels

function screenPos(riverMile) {
    riverScreenLength = riverMiles * pxPerMile;
    return headerSize + padding + riverScreenLength - (riverMile * pxPerMile)
}

// TODO: add a bunch of items here.
function writeCampsites(){

}

$(document).ready(function(){
    // jQuery methods go here...
    headerSize = $(".header").height()

    $("#rivermap").height(padding + (riverMiles * pxPerMile) + padding)

    // <!-- Consider using popovers instead of badges.-->
    $(".left-bank").append(
        $("<h5></h5>").html('<span class="badge bg-secondary">POI</span> Canyon -->')
        .css("transform", `translateY(${screenPos(100)}px)`))
  
});