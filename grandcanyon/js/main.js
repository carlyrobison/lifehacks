const riverMiles = 300;
const pxPerMile = 100;
const padding = 20;  // pixels
var headerSize = 0;  // pixels

function screenPos(riverMile) {
    riverScreenLength = riverMiles * pxPerMile;
    return headerSize + padding + riverScreenLength - (riverMile * pxPerMile)
}

function writeCampsites(){
    $.get("data/Grand Canyon POIs - Camps.csv", function(csvdata) {
        // csv is populated with the file contents
        var data = $.csv.toObjects(csvdata);
        for (const camp of data) {
            // Consider using popovers instead of badges.
            if (camp['Side'] == 'L') {
                $(".left-bank").append(
                    $("<p></p>").html('<span class="badge bg-primary">Camp</span> ' + camp['Name'] + ' -->')
                    .css("transform", `translateY(${screenPos(parseFloat(camp['River Mile']))}px)`))
            } else if (camp['Side'] == 'R') {
                $(".right-bank").append(
                    $("<p></p>").html('<-- ' + camp['Name'] + ' <span class="badge bg-primary">Camp</span>')
                    .css("transform", `translateY(${screenPos(parseFloat(camp['River Mile']))}px)`))
            } else {
                console.log('Improper side for camp:' + camp)
            }
        }
    });
}



$(document).ready(function(){
    // jQuery methods go here...
    headerSize = $(".header").height()

    $("#rivermap").height(padding + (riverMiles * pxPerMile) + padding)

    // <!-- Consider using popovers instead of badges.-->
    $(".left-bank").append(
        $("<h5></h5>").html('<span class="badge bg-secondary">POI</span> Canyon -->')
        .css("transform", `translateY(${screenPos(100)}px)`))

    writeCampsites();
  
});