$(document).ready(() => {
    $.ajax({
        type: 'GET',
        url: 'localhost:5500/flight',
        xhrFields: {
            withCredentials: true
        },
        success: res => {
            console.log(res);
            var flight_details = res.parseJSON();

        }
    });
    
    $('#form').on('submit', (e) => {
        e.preventDefault();
        window.location.href = "/travel.html";
    });
});