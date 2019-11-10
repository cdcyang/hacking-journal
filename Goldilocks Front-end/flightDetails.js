$(document).ready(() => {
    var flight_details = atob(window.location.href.split('=')[1]);
    var details = JSON.parse(flight_details);
    // console.log(flight_details);
    // var flight_details = flight_details.parseJSON();

    $('.departure_airport').html(details.departure.iataCode);
    $('.arrival_airport').html(details.arrival.iataCode);
    $('.departure_time').html(details.departure.at.split('T')[1]);
    $('.arrival_time').html(details.arrival.at.split('T')[1]);
    // $.ajax({
    //     type: 'GET',
    //     url: 'localhost:5000/flight?code=' + details.depar,
    //     xhrFields: {
    //         withCredentials: true
    //     },
    //     success: res => {
    //         var data = JSON.parse(res);
    //         $('.departure_airport').html(data.departure.iataCode);
    //         $('.arrival_airport').html(data.arrival.iataCode);
    //         $('.departure_time').html(data.departure.at.split('T')[1]);
    //         $('.arrival_time').html(data.arrival.at.split('T')[1]);
    //     }
    // });
    
    $('.form').on('submit', (e) => {
        e.preventDefault();
        // var encodedData = btoa(details.departure.iataCode);
        var encodedData = btoa({
            "testing" : "123"
        });
        window.location.href = "../html/travel.html?data=" + encodedData;
    });
});