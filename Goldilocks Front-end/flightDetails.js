$(document).ready(() => {
    var data = atob(window.location.href.split('=')[1]);
    console.log(data);
    $.ajax({
        type: 'GET',
        url: 'localhost:5500/flight',
        xhrFields: {
            withCredentials: true
        },
        success: res => {
            console.log(res);
            var flight_details = res.parseJSON();
            $('.airline').html = flight_details.airline_info.name;
        }
    });
    
    $('#form').on('submit', (e) => {
        e.preventDefault();
        window.location.href = "travel.html";
    });
});