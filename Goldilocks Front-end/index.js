$(document).ready(() => {
    $('.flightNoForm').on('submit', (e) => {
        e.preventDefault();
        var flight_number = $('#flight_number').val();
        // var regex = /^\b[A-Z]{2}\d{3,4}\b$/;
        var regex = /^\b[A-Z]{3}\b$/;
        if(flight_number.match(regex)){
            //Call back-end...
            //sendFlightNumber(flight_number);
            $('.invalid_message').html('');
            var jsonData = {
                "airline_info" : {
                    "code"  : flight_number,
                    "name" : "London Heathrow Airport"
                },
            };
            var encodedData = btoa(JSON.stringify(jsonData));
            window.location.href = "../html/flightDetails.html?data=" + encodedData;
        } else {
            $('.invalid_message').html('<p>Flight number is incorrect, please enter a valid flight number.</p>');
        }
    });

    function sendFlightNumber(flight_number) {
        $.ajax({
            type: 'GET',
            url: 'localhost:5500/flight',
            xhrFields: {
                withCredentials: true
            },
            data: flight_number,
            success: res => {
                console.log(res);
            }
        });
    }
});

//------------------FlightNO JS----------------------
// var emailInput = document.getElementById("email");
// var format = document.getElementById("format");

// // SHOW BOX
// emailInput.onfocus = function () {
//     document.getElementById("messageE").style.display = "block";
// }
// // REMOVE BOX
// emailInput.onblur = function () {
//     document.getElementById("messageE").style.display = "none";

// }
// // VALIDATE EMAIL
// emailInput.onkeyup = function () {
//     var regex = /^(\b[A-Z]{2}\d{3,4}\b))$/;
//     if(emailInput.value.match(regex)){
//         format.classList.remove("invalid");
//         format.classList.add("valid");
//     } else {
//         format.classList.remove("valid");
//         format.classList.add("invalid");
//     }
// }
