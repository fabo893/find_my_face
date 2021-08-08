#!/usr/bin/nodejs

$("#btn").click(function () {
    testing();
})

function testing(){

    let json = {
        name: 'Fabo',
        email: 'jose@gmail.com',
        estado: 'soltero'
    }
    
    $.ajax({
        type: 'POST',
        url: '/upload',
        data: json,
        contentType: 'application/json',
        success: function (response) {
            if (response === true) {
                console.log('Lo he logrado');
            }
            else {
                console.log('No lo logre');
            }
        }
    });
}