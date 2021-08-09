#!/usr/bin/nodejs

$("#btn").click(function () {
    let imagen = document.getElementById('img_one');

    console.log(imagen);
})

function testing(){

    let json1 = {
        name: 'Fabo',
        email: 'jose@gmail.com',
        estado: 'soltero'
    };
    
    console.log(json1);

    let json = JSON.stringify(json1);

    $.ajax({
        type: 'POST',
        url: '/upload',
        contentType: 'application/json',
        data: json,
        success: function (response) {
            console.log(response);

            if (response === 'OK') {
                alert('Eres crack');
            }
            else {
                alert('Trili')
            }
        }
    });
}