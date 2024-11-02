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
    var left_bank = $("#left-bank-canvas").get(0).getContext("2d")
    left_bank.textAlign = "right"
    left_bank.textBaseline = "middle"
    left_bank.font = '14pt Arial'

    var right_bank = $("#right-bank-canvas").get(0).getContext("2d")
    right_bank.textAlign = "left"
    right_bank.textBaseline = "middle"
    right_bank.font = '14pt Arial'

    var river = $("#river-canvas").get(0).getContext("2d")
    river.textAlign = "center"
    river.textBaseline = "middle"
    river.font = '14pt Arial'
}

function writeCampsites(){
    $.get("data/Grand Canyon POIs - Camps.csv", function(csvdata) {
        // csv is populated with the file contents
        var data = $.csv.toObjects(csvdata);
        var left_bank = $("#left-bank-canvas").get(0).getContext("2d")
        var right_bank = $("#right-bank-canvas").get(0).getContext("2d")
        for (const camp of data) {
            // Consider using popovers instead of badges.
            var location = screenPos(parseFloat(camp['River Mile']))
            if (camp['Side'] == 'L') {
                left_bank.fillText("[Camp] " + camp["Name"] + " -->", 500, location)
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
        var left_bank = $("#left-bank-canvas").get(0).getContext("2d")
        var right_bank = $("#right-bank-canvas").get(0).getContext("2d")
        for (const poi of data) {
            var location = screenPos(parseFloat(poi['River Mile']))
            if ((poi['Side'] == 'L') || (poi['Side'] == 'Both')) {
                left_bank.fillText("[POI] " + poi["Name"] + " -->", 500, location)
            } if ((poi['Side'] == 'R') || (poi['Side'] == 'Both')) {
                right_bank.fillText("<-- " + poi["Name"] + " [POI]", 0, location)
            }
        }
    });
}

function writeRapids(){
    $.get("data/Grand Canyon POIs - Rapids.csv", function(csvdata) {
        var data = $.csv.toObjects(csvdata);
        var river = $("#river-canvas").get(0).getContext("2d")
        for (const rapid of data) {
            var location = screenPos(parseFloat(rapid['River Mile']))
            if (parseInt(rapid['Rating']) > 5) {  // Bad rapids are warnings
                river.fillText(rapid['Name'] + "(" + rapid['Rating'] + ")", 150, location)
            } else { // Easier rapid
                river.fillText(rapid['Name'] + "(" + rapid['Rating'] + ")", 150, location)
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