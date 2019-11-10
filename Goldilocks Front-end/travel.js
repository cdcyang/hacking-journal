$(document).ready(() => {
    var airport_code = atob(window.location.href.split('=')[1]);

    $.ajax({
        type: 'GET',
        url: 'localhost:5000/route?code=' + airport_code,
        xhrFields: {
            withCredentials: true
        },
        success: res => {
            var route = JSON.parse(res);
            $('#car').html(route.car + ", £50");
            $('#public_transport').html(route.public_transport + "£2.40");
            // $('.arrival_airport').html(flight_details.arrival_info.name);
            // $('.departure_time').html(flight_details.departure_time);
            // $('.arrival_time').html(flight_details.arrival_time);
        }
    });

});
