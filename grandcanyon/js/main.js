const riverMiles = 300;
const pxPerMile = 100;
const padding = 100;  // pixels
var headerSize = 96;  // pixels

function screenPos(riverMile) {
    riverScreenLength = riverMiles * pxPerMile;
    return padding + riverScreenLength - (riverMile * pxPerMile)
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

function writePOIs(){
    $.get("data/Grand Canyon POIs - POIs.csv", function(csvdata) {
        var data = $.csv.toObjects(csvdata);
        for (const poi of data) {
            if (poi['Side'] == 'L') {
                $(".left-bank").append(
                    $("<p></p>").html('<span class="badge bg-secondary">POI</span> ' + poi['Name'] + ' -->')
                    .css("transform", `translateY(${screenPos(parseFloat(poi['River Mile']))}px)`))
            } else if (poi['Side'] == 'R') {
                $(".right-bank").append(
                    $("<p></p>").html('<-- ' + poi['Name'] + ' <span class="badge bg-secondary">POI</span>')
                    .css("transform", `translateY(${screenPos(parseFloat(poi['River Mile']))}px)`))
            } else {
                console.log('Improper side for POI:' + poi)
            }
        }
    });
}

function writeRapids(){
    $.get("data/Grand Canyon POIs - Rapids.csv", function(csvdata) {
        var data = $.csv.toObjects(csvdata);
        for (const rapid of data) {
            console.log(rapid)
            if (parseInt(rapid['Rating']) > 5) {  // Bad rapids are warnings
                $(".river").append(
                    $("<p></p>").html(rapid['Name'] + ' <span class="badge bg-danger">' + rapid['Rating'] + '</span> ')
                    .css("transform", `translateY(${screenPos(parseFloat(rapid['River Mile']))}px)`))
            } else { // Easier rapid
                $(".river").append(
                    $("<p></p>").html(rapid['Name'] + ' <span class="badge bg-warning text-dark">' + rapid['Rating'] + '</span> ')
                    .css("transform", `translateY(${screenPos(parseFloat(rapid['River Mile']))}px)`))
            }
            
        }
    });
}

$(document).ready(function(){
    // jQuery methods go here...
    headerSize = $(".header").height()

    $("#rivermap").height(padding + (riverMiles * pxPerMile) + padding)

    writePOIs();
    writeCampsites();
    writeRapids();
  
});