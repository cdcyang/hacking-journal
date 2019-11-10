$(document).ready(() => {
    var flight_details = atob(window.location.href.split('=')[1]);
    flight_details = JSON.parse(flight_details);
    // console.log(flight_details);
    // var flight_details = flight_details.parseJSON();
    $('.airline').html(flight_details.airline_info.airline);
    $('.departure_airport').html(flight_details.airline_info.name);
    // $('.arrival_airport').html(flight_details.arrival_info.name);
    // $('.departure_time').html(flight_details.departure_time);
    // $('.arrival_time').html(flight_details.arrival_time);
    $.ajax({
        type: 'GET',
        url: 'localhost:5500/flight',
        xhrFields: {
            withCredentials: true
        },
        success: res => {
        }
    });
    
    $('#form').on('submit', (e) => {
        e.preventDefault();
        window.location.href = "travel.html";
    });
});