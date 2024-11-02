const riverMiles = 300;
const pxPerMile = 100;
const padding = 100;  // pixels
var headerSize = 96;  // pixels

function screenPos(riverMile) {
    riverScreenLength = riverMiles * pxPerMile;
    return padding + riverScreenLength - (riverMile * pxPerMile)
}

function setupCanvas() {
    $("#rivermap").height(padding + (riverMiles * pxPerMile) + padding)
    var left_bank = $("#left-bank-canvas").getContext("2d")
    left_bank.textAlign = "right"
    left_bank.textBaseline = "middle"

    var right_bank = $("#right-bank-canvas").getContext("2d")
    right_bank.textAlign = "left"
    left_bank.textBaseline = "middle"

    var river = $("#river-canvas").getContext("2d")
    river.textAlign = "center"
    river.textBaseline = "middle"
}

function writeCampsites(){
    $.get("data/Grand Canyon POIs - Camps.csv", function(csvdata) {
        // csv is populated with the file contents
        var data = $.csv.toObjects(csvdata);
        var left_bank = $("#left-bank-canvas").getContext("2d")
        var right_bank = $("#right-bank-canvas").getContext("2d")
        for (const camp of data) {
            // Consider using popovers instead of badges.
            var location = screenPos(parseFloat(camp['River Mile']))
            if (camp['Side'] == 'L') {
                left_bank.fillText("[Camp] " + camp["Name"] + " -->", 100, 100)
            } else if (camp['Side'] == 'R') {
                right_bank.fillText("<-- " + camp["Name"] + " [Camp]", 0, location)
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
            if ((poi['Side'] == 'L') || (poi['Side'] == 'Both')) {
                $("#left-bank-canvas").append(
                    $("<p></p>").html('<span class="badge bg-secondary">POI</span> ' + poi['Name'] + ' -->')
                    .css("transform", `translateY(${screenPos(parseFloat(poi['River Mile']))}px)`))
            } if ((poi['Side'] == 'R') || (poi['Side'] == 'Both')) {
                $("#right-bank-canvas").append(
                    $("<p></p>").html('<-- ' + poi['Name'] + ' <span class="badge bg-secondary">POI</span>')
                    .css("transform", `translateY(${screenPos(parseFloat(poi['River Mile']))}px)`))
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

    setupCanvas();


    writePOIs();
    writeCampsites();
    writeRapids();
  
});