const riverMiles = 220;
const pxPerMile = 50;
const padding = 20;  // pixels
var headerSize = 0;  // pixels

function screenPos(riverMile) {
    riverScreenLength = riverMiles * pxPerMile;
    return headerSize + padding + riverScreenLength - (riverMile * pxPerMile)
}

$(document).ready(function(){
    // jQuery methods go here...
    headerSize = $(".header").height()

    $("#rivermap").height(padding + (riverMiles * pxPerMile) + padding)

    // TODO: add a bunch of thingies
    // <!-- Consider using popovers instead of badges.-->
    // <h3><span class="badge bg-secondary">POI</span> Canyon --></h3>
    // Why is it not showing badges?

    $(".left-bank").append(
        $("<h5></h5>").append($("<span></span>").text("POI").addClass("badge").addClass("bg-secondary"))
        .text("Canyon")
        .css("transform", `translateY(${screenPos(100)}px)`))
  
  });