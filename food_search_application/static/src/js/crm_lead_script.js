$(document).ready(function () {
    $("button[name=get_latitude_longitude]").click(function () {
        console.log('testing1------------------')
        var latitude = $("div[name=latitude]").find("input").val();
        var longitude = $("div[name=longitude]").find("input").val();

        // Use latitude and longitude as needed
        console.log('testing2------------------')
        console.log("Latitude:11 ", latitude);
        console.log("Longitude:11 ", longitude);
    });
});
